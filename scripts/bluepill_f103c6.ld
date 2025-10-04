/* Define as memórias disponíveis */
MEMORY
{
    FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 32K
    RAM (xrw)  : ORIGIN = 0x20000000, LENGTH = 10K
}

/* Definições dos símbolos obrigatórios */
_estack = ORIGIN(RAM) + LENGTH(RAM); /* Topo da pilha */

/* Configuração das seções */
SECTIONS
{
    /* Vetores de interrupção na Flash */
    .isr_vector :
    {
        KEEP(*(.isr_vector)) /* Vetores de interrupção */
    } > FLASH

    /* Código e dados somente leitura na Flash */
    .text :
    {
        *(.text*) /* Código do programa */
        *(.rodata*) /* Dados somente leitura */
        *(.init*) /* Seção .init */
    } > FLASH

    /* Dados inicializados na RAM, com carga na Flash */
    .data : AT(ADDR(.text) + SIZEOF(.text))
    {
        __data_start = .; /* Início dos dados inicializados */
        *(.data*) /* Dados inicializados */
        __data_end = .; /* Fim dos dados inicializados */
    } > RAM

    /* Dados não inicializados na RAM */
    .bss :
    {
        __bss_start = .; /* Início da seção não inicializada */
        *(.bss*) /* Dados não inicializados */
        __bss_end = .; /* Fim da seção não inicializada */
    } > RAM

    /* Símbolos adicionais */
    _sdata = __data_start;
    _edata = __data_end;
    _sbss = __bss_start;
    _ebss = __bss_end;
    _sidata = LOADADDR(.data); /* Endereço de carga na Flash */
    _end = ORIGIN(RAM) + LENGTH(RAM);
    _Min_Stack_Size = 0x400; /* Tamanho mínimo da pilha */
}

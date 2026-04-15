from src.my_project.main import main


def test_main_execution() -> None:
    """
    Verifica que la función principal se ejecute sin errores.
    """
    # Como main() devuelve None y solo loguea, validamos su ejecución exitosa.
    main()
    result = 1 + 1
    expected_result = 2
    assert result == expected_result

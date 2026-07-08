from pages.carbohydrate_calculator_page import CarbohydrateCalculatorPage

def test_metric_valid_inputs(driver):

    page = CarbohydrateCalculatorPage(driver)

    page.open()

    page.select_metric()

    page.select_gender("male")

    page.set_metric_values(
        age="25",
        height="175",
        weight="75"
    )

    page.select_activity("Light: exercise 1-3 times/week")

    page.calculate()

    assert page.results_displayed()

def test_us_valid_inputs(driver):

    page = CarbohydrateCalculatorPage(driver)

    page.open()

    page.select_us()

    page.select_gender("female")

    page.set_us_values(
        age="25",
        feet="5",
        inches="9",
        weight="160"
    )

    page.select_activity("Moderate: exercise 4-5 times/week")

    page.calculate()

    assert page.results_displayed()


def test_upper_age_boundary(driver):

    page = CarbohydrateCalculatorPage(driver)

    page.open()

    page.select_metric()

    page.select_gender("male")

    page.set_metric_values(
        age="80",
        height="170",
        weight="60"
    )

    page.select_activity("Light: exercise 1-3 times/week")

    page.calculate()

    assert page.results_displayed()


def test_weight_zero(driver):

    page = CarbohydrateCalculatorPage(driver)

    page.open()

    page.select_metric()

    page.select_gender("male")

    page.set_metric_values(
        age="80",
        height="170",
        weight="0"
    )

    page.select_activity("Light: exercise 1-3 times/week")

    page.calculate()

    assert page.invalid_input_error("Please provide positive weight value.")


def test_weight_alpha(driver):

    page = CarbohydrateCalculatorPage(driver)

    page.open()

    page.select_metric()

    page.select_gender("female")

    page.set_metric_values(
        age="80",
        height="170",
        weight="ABC"
    )

    page.select_activity("Light: exercise 1-3 times/week")

    page.calculate()

    assert page.invalid_input_error("Please provide positive weight value.")
/*
  generic Baro driver test
 */

#include <AP_HAL/AP_HAL.h>
#include <AP_Baro/AP_Baro.h>

const AP_HAL::HAL& hal = AP_HAL::get_HAL();

static AP_Baro barometer;

static uint32_t timer;
static uint8_t counter;

void setup()
{
    hal.console->println("Barometer library test");

    hal.scheduler->delay(1000);

#if CONFIG_HAL_BOARD == HAL_BOARD_APM2
    // disable CS on MPU6000
    hal.gpio->pinMode(63, HAL_GPIO_OUTPUT);
    hal.gpio->write(63, 1);
#endif

    barometer.init();
    barometer.calibrate();

    timer = hal.scheduler->micros();
}

void loop()
{
    // run accumulate() at 50Hz and update() at 10Hz
    if((hal.scheduler->micros() - timer) > 20*1000UL) {
        timer = hal.scheduler->micros();
        barometer.accumulate();
        if (counter++ < 5) {
            return;
        }
        counter = 0;
        barometer.update();
        uint32_t read_time = hal.scheduler->micros() - timer;
        float alt = barometer.get_altitude();
        if (!barometer.healthy()) {
            hal.console->println("not healthy");
            return;
        }
        hal.console->print("Pressure:");
        hal.console->print(barometer.get_pressure());
        hal.console->print(" Temperature:");
        hal.console->print(barometer.get_temperature());
        hal.console->print(" Altitude:");
        hal.console->print(alt);
        hal.console->printf(" climb=%.2f t=%u",
                            barometer.get_climb_rate(),
                            (unsigned)read_time);
        hal.console->println();
    } else {
        hal.scheduler->delay(1);
    }
}

AP_HAL_MAIN();

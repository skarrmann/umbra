# Umbra GP2040-CE Configuration

Follow the [installation instructions at the GP2040-CE Firmware documentation](https://gp2040-ce.info/#/?id=installation).

Once the GP2040-CE firmware has been flashed onto the Pi Pico, configure the board with the [GP2040 Web Configurator](https://gp2040.info/#/web-configurator). In the initial firmware, the `S2` key is mapped to `GP17`, which is the furthest right bottom key on the Umbra. So to activate the web configurator, hold this key when plugging in the board.

In the GP2040 Configurator, apply the configuration:

1. In **Configuration > Pin Mapping**, set your preferred pin mapping. Here is the Umbra Pi Pico GPIO pin assignment:
    ![Umbra Pi Pico GPIO](/images/umbra-pi-pico-gpio.png)
2. In **Configuration > LED Configuration**, set "Data Pin" to `-1` and click **Save**.
3. (Optional) In **Configuration > Add Ons**, disable all options and click **Save**.
4. Once done, click **Reboot**.
from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (TC_DisplayModes, TC_SensorTypes)
from .definitions.structures import (TC_LoopParameters, TLI_DeviceInfo, TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.TEC.DLL")

TC_CheckConnection = lib.TC_CheckConnection
TC_CheckConnection.restype = c_bool
TC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = TC_CheckConnection(serial_number)

    return output


TC_ClearMessageQueue = lib.TC_ClearMessageQueue
TC_ClearMessageQueue.restype = c_void_p
TC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = TC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_Close = lib.TC_Close
TC_Close.restype = c_void_p
TC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = TC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_Disable = lib.TC_Disable
TC_Disable.restype = c_short
TC_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    # Disable cube.

    serial_number = POINTER(c_char)

    output = TC_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_Disconnect = lib.TC_Disconnect
TC_Disconnect.restype = c_short
TC_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = TC_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_Enable = lib.TC_Enable
TC_Enable.restype = c_short
TC_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable cube for computer control.

    serial_number = POINTER(c_char)

    output = TC_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_EnableLastMsgTimer = lib.TC_EnableLastMsgTimer
TC_EnableLastMsgTimer.restype = c_void_p
TC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = TC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


TC_GetCurrentLimit = lib.TC_GetCurrentLimit
TC_GetCurrentLimit.restype = c_long
TC_GetCurrentLimit.argtypes = [POINTER(c_char)]


def get_current_limit(serial_number):
    # Gets the max current limit.

    serial_number = POINTER(c_char)

    output = TC_GetCurrentLimit(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetCurrentReading = lib.TC_GetCurrentReading
TC_GetCurrentReading.restype = c_long
TC_GetCurrentReading.argtypes = [POINTER(c_char)]


def get_current_reading(serial_number):
    # Gets current reading.

    serial_number = POINTER(c_char)

    output = TC_GetCurrentReading(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetFirmwareVersion = lib.TC_GetFirmwareVersion
TC_GetFirmwareVersion.restype = c_ulong
TC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = TC_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetHWDisplayMode = lib.TC_GetHWDisplayMode
TC_GetHWDisplayMode.restype = TC_DisplayModes
TC_GetHWDisplayMode.argtypes = [POINTER(c_char)]


def get_h_w_display_mode(serial_number):
    # Gets the display mode / output mode for the device.

    serial_number = POINTER(c_char)

    output = TC_GetHWDisplayMode(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetHardwareInfo = lib.TC_GetHardwareInfo
TC_GetHardwareInfo.restype = c_short
TC_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]


def get_hardware_info(serial_number):
    # Gets the hardware information from the device.

    serial_number = POINTER(c_char)
    modelNo = POINTER(c_char)
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = TC_GetHardwareInfo(
        serial_number,
        modelNo,
        sizeOfModelNo,
        type,
        numChannels,
        notes,
        sizeOfNotes,
        firmwareVersion,
        hardwareVersion,
        modificationState)
    if output != 0:
        raise KinesisException(output)


TC_GetHardwareInfoBlock = lib.TC_GetHardwareInfoBlock
TC_GetHardwareInfoBlock.restype = c_short
TC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = TC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


TC_GetLEDBrightness = lib.TC_GetLEDBrightness
TC_GetLEDBrightness.restype = c_short
TC_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_l_e_d_brightness(serial_number):
    # Gets the LED brightness.

    serial_number = POINTER(c_char)

    output = TC_GetLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetNextMessage = lib.TC_GetNextMessage
TC_GetNextMessage.restype = c_bool
TC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = TC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


TC_GetSensorType = lib.TC_GetSensorType
TC_GetSensorType.restype = TC_SensorTypes
TC_GetSensorType.argtypes = [POINTER(c_char)]


def get_sensor_type(serial_number):
    # Gets the sensor type.

    serial_number = POINTER(c_char)

    output = TC_GetSensorType(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetSoftwareVersion = lib.TC_GetSoftwareVersion
TC_GetSoftwareVersion.restype = c_ulong
TC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = TC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetStatusBits = lib.TC_GetStatusBits
TC_GetStatusBits.restype = c_ulong
TC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = TC_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetTempLoopParams = lib.TC_GetTempLoopParams
TC_GetTempLoopParams.restype = c_short
TC_GetTempLoopParams.argtypes = [POINTER(c_char), TC_LoopParameters]


def get_temp_loop_params(serial_number):
    # Gets the temperature loop parameters.

    serial_number = POINTER(c_char)
    proportionalIntegralDerivativeParams = TC_LoopParameters()

    output = TC_GetTempLoopParams(serial_number, proportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


TC_GetTemperatureReading = lib.TC_GetTemperatureReading
TC_GetTemperatureReading.restype = c_short
TC_GetTemperatureReading.argtypes = [POINTER(c_char)]


def get_temperature_reading(serial_number):
    # Gets temperature reading.

    serial_number = POINTER(c_char)

    output = TC_GetTemperatureReading(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_GetTemperatureSet = lib.TC_GetTemperatureSet
TC_GetTemperatureSet.restype = c_short
TC_GetTemperatureSet.argtypes = [POINTER(c_char)]


def get_temperature_set(serial_number):
    # Gets the required temperature.

    serial_number = POINTER(c_char)

    output = TC_GetTemperatureSet(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_HasLastMsgTimerOverrun = lib.TC_HasLastMsgTimerOverrun
TC_HasLastMsgTimerOverrun.restype = c_bool
TC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by TC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = TC_HasLastMsgTimerOverrun(serial_number)

    return output


TC_Identify = lib.TC_Identify
TC_Identify.restype = c_void_p
TC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = TC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_LoadNamedSettings = lib.TC_LoadNamedSettings
TC_LoadNamedSettings.restype = c_bool
TC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = TC_LoadNamedSettings(serial_number, settingsName)

    return output


TC_LoadSettings = lib.TC_LoadSettings
TC_LoadSettings.restype = c_bool
TC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = TC_LoadSettings(serial_number)

    return output


TC_MessageQueueSize = lib.TC_MessageQueueSize
TC_MessageQueueSize.restype = c_int
TC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = TC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_Open = lib.TC_Open
TC_Open.restype = c_short
TC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = TC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_PersistSettings = lib.TC_PersistSettings
TC_PersistSettings.restype = c_bool
TC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = TC_PersistSettings(serial_number)

    return output


TC_PollingDuration = lib.TC_PollingDuration
TC_PollingDuration.restype = c_long
TC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = TC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RegisterMessageCallback = lib.TC_RegisterMessageCallback
TC_RegisterMessageCallback.restype = c_void_p
TC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = TC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


TC_RequestCurrentLimit = lib.TC_RequestCurrentLimit
TC_RequestCurrentLimit.restype = c_short
TC_RequestCurrentLimit.argtypes = [POINTER(c_char)]


def request_current_limit(serial_number):
    # Requests the device current limit.

    serial_number = POINTER(c_char)

    output = TC_RequestCurrentLimit(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestHWDisplayMode = lib.TC_RequestHWDisplayMode
TC_RequestHWDisplayMode.restype = c_short
TC_RequestHWDisplayMode.argtypes = [POINTER(c_char)]


def request_h_w_display_mode(serial_number):
    # Requests the quantity displayed by hardware.

    serial_number = POINTER(c_char)

    output = TC_RequestHWDisplayMode(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestLEDBrightness = lib.TC_RequestLEDBrightness
TC_RequestLEDBrightness.restype = c_short
TC_RequestLEDBrightness.argtypes = [POINTER(c_char)]


def request_l_e_d_brightness(serial_number):
    # Requests the LED brightness.

    serial_number = POINTER(c_char)

    output = TC_RequestLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestReadings = lib.TC_RequestReadings
TC_RequestReadings.restype = c_short
TC_RequestReadings.argtypes = [POINTER(c_char)]


def request_readings(serial_number):
    # Requests temperature and current readings.

    serial_number = POINTER(c_char)

    output = TC_RequestReadings(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestSensorType = lib.TC_RequestSensorType
TC_RequestSensorType.restype = c_short
TC_RequestSensorType.argtypes = [POINTER(c_char)]


def request_sensor_type(serial_number):
    # Requests the sensor type.

    serial_number = POINTER(c_char)

    output = TC_RequestSensorType(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestSettings = lib.TC_RequestSettings
TC_RequestSettings.restype = c_short
TC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = TC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestStatus = lib.TC_RequestStatus
TC_RequestStatus.restype = c_short
TC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the state quantities (actual temperature, current and status bits).

    serial_number = POINTER(c_char)

    output = TC_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestStatusBits = lib.TC_RequestStatusBits
TC_RequestStatusBits.restype = c_short
TC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = TC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestTempLoopParams = lib.TC_RequestTempLoopParams
TC_RequestTempLoopParams.restype = c_short
TC_RequestTempLoopParams.argtypes = [POINTER(c_char)]


def request_temp_loop_params(serial_number):
    # Requests the temperature loop parameters.

    serial_number = POINTER(c_char)

    output = TC_RequestTempLoopParams(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_RequestTemperatureSet = lib.TC_RequestTemperatureSet
TC_RequestTemperatureSet.restype = c_short
TC_RequestTemperatureSet.argtypes = [POINTER(c_char)]


def request_temperature_set(serial_number):
    # Requests the set temperature.

    serial_number = POINTER(c_char)

    output = TC_RequestTemperatureSet(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_Reset = lib.TC_Reset
TC_Reset.restype = c_short
TC_Reset.argtypes = [POINTER(c_char)]


def reset(serial_number):
    # Reset the device.

    serial_number = POINTER(c_char)

    output = TC_Reset(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_SetCurrentLimit = lib.TC_SetCurrentLimit
TC_SetCurrentLimit.restype = c_short
TC_SetCurrentLimit.argtypes = [POINTER(c_char), c_long]


def set_current_limit(serial_number):
    # Sets the max current limit.

    serial_number = POINTER(c_char)
    maxCurrent = c_long()

    output = TC_SetCurrentLimit(serial_number, maxCurrent)
    if output != 0:
        raise KinesisException(output)


TC_SetHWDisplayMode = lib.TC_SetHWDisplayMode
TC_SetHWDisplayMode.restype = c_short
TC_SetHWDisplayMode.argtypes = [POINTER(c_char), TC_DisplayModes]


def set_h_w_display_mode(serial_number):
    # Sets the display mode / output mode for the device.

    serial_number = POINTER(c_char)
    mode = TC_DisplayModes()

    output = TC_SetHWDisplayMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


TC_SetLEDBrightness = lib.TC_SetLEDBrightness
TC_SetLEDBrightness.restype = c_short
TC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_l_e_d_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = POINTER(c_char)
    brightness = c_short()

    output = TC_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


TC_SetSensorType = lib.TC_SetSensorType
TC_SetSensorType.restype = c_short
TC_SetSensorType.argtypes = [POINTER(c_char), TC_SensorTypes]


def set_sensor_type(serial_number):
    # Sets the sensor type.

    serial_number = POINTER(c_char)
    sensor = TC_SensorTypes()

    output = TC_SetSensorType(serial_number, sensor)
    if output != 0:
        raise KinesisException(output)


TC_SetTempLoopParams = lib.TC_SetTempLoopParams
TC_SetTempLoopParams.restype = c_short
TC_SetTempLoopParams.argtypes = [POINTER(c_char), TC_LoopParameters]


def set_temp_loop_params(serial_number):
    # Sets the temperature loop parameters.

    serial_number = POINTER(c_char)
    proportionalIntegralDerivativeParams = TC_LoopParameters()

    output = TC_SetTempLoopParams(serial_number, proportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


TC_SetTemperature = lib.TC_SetTemperature
TC_SetTemperature.restype = c_short
TC_SetTemperature.argtypes = [POINTER(c_char), c_short]


def set_temperature(serial_number):
    # Sets the required temperature.

    serial_number = POINTER(c_char)
    temperature = c_short()

    output = TC_SetTemperature(serial_number, temperature)
    if output != 0:
        raise KinesisException(output)


TC_StartPolling = lib.TC_StartPolling
TC_StartPolling.restype = c_bool
TC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = TC_StartPolling(serial_number, milliseconds)

    return output


TC_StopPolling = lib.TC_StopPolling
TC_StopPolling.restype = c_void_p
TC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = TC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


TC_TimeSinceLastMsgReceived = lib.TC_TimeSinceLastMsgReceived
TC_TimeSinceLastMsgReceived.restype = c_bool
TC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = TC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


TC_WaitForMessage = lib.TC_WaitForMessage
TC_WaitForMessage.restype = c_bool
TC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = TC_WaitForMessage(serial_number, messageType, messageID, messageData)

    return output


TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = [c_void_p]


def build_device_list():
    # Build the DeviceList.

    output = TLI_BuildDeviceList()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]


def get_device_info(serial_number):
    # Get the device information from the USB port.

    serial_number = POINTER(c_char)
    serialNumber = POINTER(c_char)
    info = TLI_DeviceInfo()

    output = TLI_GetDeviceInfo(serial_number, serialNumber, info)
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]


def get_device_list():
    # Get the entire contents of the device list.

    output = TLI_GetDeviceList()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]


def get_device_list_by_type():
    # Get the contents of the device list which match the supplied typeID.

    output = TLI_GetDeviceListByType()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]


def get_device_list_by_type_ext():
    # Get the contents of the device list which match the supplied typeID.

    output = TLI_GetDeviceListByTypeExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]


def get_device_list_by_types():
    # Get the contents of the device list which match the supplied typeIDs.

    output = TLI_GetDeviceListByTypes()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_ulong, c_int, c_int]


def get_device_list_by_types_ext():
    # Get the contents of the device list which match the supplied typeIDs.

    output = TLI_GetDeviceListByTypesExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]


def get_device_list_ext():
    # Get the entire contents of the device list.

    output = TLI_GetDeviceListExt()
    if output != 0:
        raise KinesisException(output)


TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short


def get_device_list_size():
    # Gets the device list size.

    output = TLI_GetDeviceListSize()
    if output != 0:
        raise KinesisException(output)


TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p


def initialize_simulations():
    # Initialize a connection to the Simulation Manager, which must already be running.

    output = TLI_InitializeSimulations()
    if output != 0:
        raise KinesisException(output)

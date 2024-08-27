from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_char_p,
    c_int,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    TC_DisplayModes,
    TC_SensorTypes)
from .definitions.structures import (
    TC_LoopParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException

c_short_pointer = type(pointer(c_short()))
c_ulong_pointer = type(pointer(c_ulong()))
c_long_pointer = type(pointer(c_ulong()))


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.TCube.TEC.DLL")

TC_CheckConnection = lib.TC_CheckConnection
TC_CheckConnection.restype = c_bool
TC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    '''
    Check connection.

    Parameters
    ----------
    serial_number - int
        serial_number of instrument

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_CheckConnection(serial_number)

    return output


TC_ClearMessageQueue = lib.TC_ClearMessageQueue
TC_ClearMessageQueue.restype = c_void_p
TC_ClearMessageQueue.argtypes = []


def clear_message_queue(serial_number):
    '''
    Clears the device message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_ClearMessageQueue(serial_number)

    return output


TC_Close = lib.TC_Close
TC_Close.restype = c_void_p
TC_Close.argtypes = []


def close_device(serial_number):
    '''
    Disconnect and close the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_Close(serial_number)

    return output


TC_Disable = lib.TC_Disable
TC_Disable.restype = c_short
TC_Disable.argtypes = []


def disable(serial_number):
    '''
    Disable cube.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_Disable(serial_number)

    return output


TC_Disconnect = lib.TC_Disconnect
TC_Disconnect.restype = c_short
TC_Disconnect.argtypes = []


def disconnect(serial_number):
    '''
    Tells the device that it is being disconnected.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_Disconnect(serial_number)

    return output


TC_Enable = lib.TC_Enable
TC_Enable.restype = c_short
TC_Enable.argtypes = []


def enable(serial_number):
    '''
    Enable cube for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_Enable(serial_number)

    return output


TC_EnableLastMsgTimer = lib.TC_EnableLastMsgTimer
TC_EnableLastMsgTimer.restype = c_void_p
TC_EnableLastMsgTimer.argtypes = []


def enable_last_msg_timer(serial_number):
    '''
    Enables the last message monitoring timer.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        enable: c_bool
        lastMsgTimeout: c_int32

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = TC_EnableLastMsgTimer(serial_number)

    return output


TC_GetCurrentLimit = lib.TC_GetCurrentLimit
TC_GetCurrentLimit.restype = c_long
TC_GetCurrentLimit.argtypes = []


def get_current_limit(serial_number):
    '''
    Gets the max current limit.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetCurrentLimit(serial_number)

    return output


TC_GetCurrentReading = lib.TC_GetCurrentReading
TC_GetCurrentReading.restype = c_long
TC_GetCurrentReading.argtypes = []


def get_current_reading(serial_number):
    '''
    Gets current reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetCurrentReading(serial_number)

    return output


TC_GetFirmwareVersion = lib.TC_GetFirmwareVersion
TC_GetFirmwareVersion.restype = c_ulong
TC_GetFirmwareVersion.argtypes = []


def get_firmware_version(serial_number):
    '''
    Gets version number of the device firmware.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetFirmwareVersion(serial_number)

    return output


TC_GetHWDisplayMode = lib.TC_GetHWDisplayMode
TC_GetHWDisplayMode.restype = TC_DisplayModes
TC_GetHWDisplayMode.argtypes = []


def get_h_w_display_mode(serial_number):
    '''
    Gets the display mode / output mode for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        TC_DisplayModes
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetHWDisplayMode(serial_number)

    return output


TC_GetHardwareInfo = lib.TC_GetHardwareInfo
TC_GetHardwareInfo.restype = c_short
TC_GetHardwareInfo.argtypes = [POINTER(c_char)]


def get_hardware_info(serial_number):
    '''
    Gets the hardware information from the device.

    Parameters
    ----------
    serial_number - int
        serial_number of instrument

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = TC_GetHardwareInfo(serial_number)

    return output


TC_GetHardwareInfoBlock = lib.TC_GetHardwareInfoBlock
TC_GetHardwareInfoBlock.restype = c_short
TC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


def get_hardware_info_block(serial_number):
    '''
    Gets the hardware information in a block.

    Parameters
    ----------
    serial_number - int
        serial_number of instrument

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    hardwareInfo = TLI_HardwareInformation()

    output = TC_GetHardwareInfoBlock(serial_number)

    return output


TC_GetLEDBrightness = lib.TC_GetLEDBrightness
TC_GetLEDBrightness.restype = c_short
TC_GetLEDBrightness.argtypes = []


def get_l_e_d_brightness(serial_number):
    '''
    Gets the LED brightness.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetLEDBrightness(serial_number)

    return output


TC_GetNextMessage = lib.TC_GetNextMessage
TC_GetNextMessage.restype = c_bool
TC_GetNextMessage.argtypes = []


def get_next_message(serial_number):
    '''
    Get the next MessageQueue item.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = TC_GetNextMessage(serial_number)

    return output


TC_GetSensorType = lib.TC_GetSensorType
TC_GetSensorType.restype = TC_SensorTypes
TC_GetSensorType.argtypes = []


def get_sensor_type(serial_number):
    '''
    Gets the sensor type.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        TC_SensorTypes
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetSensorType(serial_number)

    return output


TC_GetSoftwareVersion = lib.TC_GetSoftwareVersion
TC_GetSoftwareVersion.restype = c_ulong
TC_GetSoftwareVersion.argtypes = []


def get_software_version(serial_number):
    '''
    Gets version number of the device software.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetSoftwareVersion(serial_number)

    return output


TC_GetStatusBits = lib.TC_GetStatusBits
TC_GetStatusBits.restype = c_ulong
TC_GetStatusBits.argtypes = []


def get_status_bits(serial_number):
    '''
    Get the current status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetStatusBits(serial_number)

    return output


TC_GetTempLoopParams = lib.TC_GetTempLoopParams
TC_GetTempLoopParams.restype = c_short
TC_GetTempLoopParams.argtypes = []


def get_temp_loop_params(serial_number):
    '''
    Gets the temperature loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalIntegralDerivativeParams: TC_LoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    proportionalIntegralDerivativeParams = TC_LoopParameters()

    output = TC_GetTempLoopParams(serial_number)

    return output


TC_GetTemperatureReading = lib.TC_GetTemperatureReading
TC_GetTemperatureReading.restype = c_short
TC_GetTemperatureReading.argtypes = []


def get_temperature_reading(serial_number):
    '''
    Gets temperature reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetTemperatureReading(serial_number)

    return output


TC_GetTemperatureSet = lib.TC_GetTemperatureSet
TC_GetTemperatureSet.restype = c_short
TC_GetTemperatureSet.argtypes = []


def get_temperature_set(serial_number):
    '''
    Gets the required temperature.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_GetTemperatureSet(serial_number)

    return output


TC_HasLastMsgTimerOverrun = lib.TC_HasLastMsgTimerOverrun
TC_HasLastMsgTimerOverrun.restype = c_bool
TC_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by TC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_HasLastMsgTimerOverrun(serial_number)

    return output


TC_Identify = lib.TC_Identify
TC_Identify.restype = c_void_p
TC_Identify.argtypes = []


def identify(serial_number):
    '''
    Sends a command to the device to make it identify iteself.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_Identify(serial_number)

    return output


TC_LoadNamedSettings = lib.TC_LoadNamedSettings
TC_LoadNamedSettings.restype = c_bool
TC_LoadNamedSettings.argtypes = []


def load_named_settings(serial_number):
    '''
    Update device with named settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        settingsName: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    settingsName = POINTER(c_char)()

    output = TC_LoadNamedSettings(serial_number)

    return output


TC_LoadSettings = lib.TC_LoadSettings
TC_LoadSettings.restype = c_bool
TC_LoadSettings.argtypes = []


def load_settings(serial_number):
    '''
    Update device with stored settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_LoadSettings(serial_number)

    return output


TC_MessageQueueSize = lib.TC_MessageQueueSize
TC_MessageQueueSize.restype = c_int
TC_MessageQueueSize.argtypes = []


def message_queue_size(serial_number):
    '''
    Gets the MessageQueue size.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_MessageQueueSize(serial_number)

    return output


TC_Open = lib.TC_Open
TC_Open.restype = c_short
TC_Open.argtypes = []


def open_device(serial_number):
    '''
    Open the device for communications.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_Open(serial_number)

    return output


TC_PersistSettings = lib.TC_PersistSettings
TC_PersistSettings.restype = c_bool
TC_PersistSettings.argtypes = []


def persist_settings(serial_number):
    '''
    persist the devices current settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_PersistSettings(serial_number)

    return output


TC_PollingDuration = lib.TC_PollingDuration
TC_PollingDuration.restype = c_long
TC_PollingDuration.argtypes = []


def polling_duration(serial_number):
    '''
    Gets the polling loop duration.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_PollingDuration(serial_number)

    return output


TC_RegisterMessageCallback = lib.TC_RegisterMessageCallback
TC_RegisterMessageCallback.restype = c_void_p
TC_RegisterMessageCallback.argtypes = []


def register_message_callback(serial_number):
    '''
    Registers a callback on the message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        None

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RegisterMessageCallback(serial_number)

    return output


TC_RequestCurrentLimit = lib.TC_RequestCurrentLimit
TC_RequestCurrentLimit.restype = c_short
TC_RequestCurrentLimit.argtypes = []


def request_current_limit(serial_number):
    '''
    Requests the device current limit.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestCurrentLimit(serial_number)

    return output


TC_RequestHWDisplayMode = lib.TC_RequestHWDisplayMode
TC_RequestHWDisplayMode.restype = c_short
TC_RequestHWDisplayMode.argtypes = []


def request_h_w_display_mode(serial_number):
    '''
    Requests the quantity displayed by hardware.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestHWDisplayMode(serial_number)

    return output


TC_RequestLEDBrightness = lib.TC_RequestLEDBrightness
TC_RequestLEDBrightness.restype = c_short
TC_RequestLEDBrightness.argtypes = []


def request_l_e_d_brightness(serial_number):
    '''
    Requests the LED brightness.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestLEDBrightness(serial_number)

    return output


TC_RequestReadings = lib.TC_RequestReadings
TC_RequestReadings.restype = c_short
TC_RequestReadings.argtypes = []


def request_readings(serial_number):
    '''
    Requests temperature and current readings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestReadings(serial_number)

    return output


TC_RequestSensorType = lib.TC_RequestSensorType
TC_RequestSensorType.restype = c_short
TC_RequestSensorType.argtypes = []


def request_sensor_type(serial_number):
    '''
    Requests the sensor type.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestSensorType(serial_number)

    return output


TC_RequestSettings = lib.TC_RequestSettings
TC_RequestSettings.restype = c_short
TC_RequestSettings.argtypes = []


def request_settings(serial_number):
    '''
    Requests that all settings are download from device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestSettings(serial_number)

    return output


TC_RequestStatus = lib.TC_RequestStatus
TC_RequestStatus.restype = c_short
TC_RequestStatus.argtypes = []


def request_status(serial_number):
    '''
    Requests the state quantities (actual temperature, current and status bits).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestStatus(serial_number)

    return output


TC_RequestStatusBits = lib.TC_RequestStatusBits
TC_RequestStatusBits.restype = c_short
TC_RequestStatusBits.argtypes = []


def request_status_bits(serial_number):
    '''
    Request the status bits which identify the current device state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestStatusBits(serial_number)

    return output


TC_RequestTempLoopParams = lib.TC_RequestTempLoopParams
TC_RequestTempLoopParams.restype = c_short
TC_RequestTempLoopParams.argtypes = []


def request_temp_loop_params(serial_number):
    '''
    Requests the temperature loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestTempLoopParams(serial_number)

    return output


TC_RequestTemperatureSet = lib.TC_RequestTemperatureSet
TC_RequestTemperatureSet.restype = c_short
TC_RequestTemperatureSet.argtypes = []


def request_temperature_set(serial_number):
    '''
    Requests the set temperature.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_RequestTemperatureSet(serial_number)

    return output


TC_Reset = lib.TC_Reset
TC_Reset.restype = c_short
TC_Reset.argtypes = []


def reset(serial_number):
    '''
    Reset the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_Reset(serial_number)

    return output


TC_SetCurrentLimit = lib.TC_SetCurrentLimit
TC_SetCurrentLimit.restype = c_short
TC_SetCurrentLimit.argtypes = []


def set_current_limit(serial_number):
    '''
    Sets the max current limit.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        maxCurrent: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    maxCurrent = c_long()

    output = TC_SetCurrentLimit(serial_number)

    return output


TC_SetHWDisplayMode = lib.TC_SetHWDisplayMode
TC_SetHWDisplayMode.restype = c_short
TC_SetHWDisplayMode.argtypes = []


def set_h_w_display_mode(serial_number):
    '''
    Sets the display mode / output mode for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: TC_DisplayModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = TC_DisplayModes()

    output = TC_SetHWDisplayMode(serial_number)

    return output


TC_SetLEDBrightness = lib.TC_SetLEDBrightness
TC_SetLEDBrightness.restype = c_short
TC_SetLEDBrightness.argtypes = []


def set_l_e_d_brightness(serial_number):
    '''
    Sets the LED brightness.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        brightness: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    brightness = c_short()

    output = TC_SetLEDBrightness(serial_number)

    return output


TC_SetSensorType = lib.TC_SetSensorType
TC_SetSensorType.restype = c_short
TC_SetSensorType.argtypes = []


def set_sensor_type(serial_number):
    '''
    Sets the sensor type.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        sensor: TC_SensorTypes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    sensor = TC_SensorTypes()

    output = TC_SetSensorType(serial_number)

    return output


TC_SetTempLoopParams = lib.TC_SetTempLoopParams
TC_SetTempLoopParams.restype = c_short
TC_SetTempLoopParams.argtypes = []


def set_temp_loop_params(serial_number):
    '''
    Sets the temperature loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalIntegralDerivativeParams: TC_LoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    proportionalIntegralDerivativeParams = TC_LoopParameters()

    output = TC_SetTempLoopParams(serial_number)

    return output


TC_SetTemperature = lib.TC_SetTemperature
TC_SetTemperature.restype = c_short
TC_SetTemperature.argtypes = []


def set_temperature(serial_number):
    '''
    Sets the required temperature.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        temperature: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    temperature = c_short()

    output = TC_SetTemperature(serial_number)

    return output


TC_StartPolling = lib.TC_StartPolling
TC_StartPolling.restype = c_bool
TC_StartPolling.argtypes = []


def start_polling(serial_number):
    '''
    Starts the internal polling loop which continuously requests position and status.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        milliseconds: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    milliseconds = c_int()

    output = TC_StartPolling(serial_number)

    return output


TC_StopPolling = lib.TC_StopPolling
TC_StopPolling.restype = c_void_p
TC_StopPolling.argtypes = []


def stop_polling(serial_number):
    '''
    Stops the internal polling loop.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)

    output = TC_StopPolling(serial_number)

    return output


TC_TimeSinceLastMsgReceived = lib.TC_TimeSinceLastMsgReceived
TC_TimeSinceLastMsgReceived.restype = c_bool
TC_TimeSinceLastMsgReceived.argtypes = []


def time_since_last_msg_received(serial_number):
    '''
    Gets the time in milliseconds since tha last message was received from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        lastUpdateTimeMS: c_int64

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    lastUpdateTimeMS = c_int64()

    output = TC_TimeSinceLastMsgReceived(serial_number)

    return output


TC_WaitForMessage = lib.TC_WaitForMessage
TC_WaitForMessage.restype = c_bool
TC_WaitForMessage.argtypes = []


def wait_for_message(serial_number):
    '''
    Wait for next MessageQueue item.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = TC_WaitForMessage(serial_number)

    return output


TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = []


def build_device_list():
    '''
    Build the DeviceList.

    Parameters
    ----------
        None

    Returns
    -------
        c_short
    '''


    output = TLI_BuildDeviceList()

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = []


def get_device_info(serial_number):
    '''
    Get the device information from the USB port.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        serialNumber: POINTER(c_char)
        info: TLI_DeviceInfo

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    serialNumber = POINTER(c_char)()
    info = TLI_DeviceInfo()

    output = TLI_GetDeviceInfo(serial_number)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = []


def get_device_list(stringsReceiver):
    '''
    Get the entire contents of the device list.

    Parameters
    ----------
        stringsReceiver: SafeArray

    Returns
    -------
        c_short
    '''

    stringsReceiver = SafeArray()

    output = TLI_GetDeviceList(stringsReceiver)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = []


def get_device_list_by_type(stringsReceiver):
    '''
    Get the contents of the device list which match the supplied typeID.

    Parameters
    ----------
        stringsReceiver: SafeArray
        typeID: c_int

    Returns
    -------
        c_short
    '''

    stringsReceiver = SafeArray()
    typeID = c_int()

    output = TLI_GetDeviceListByType(stringsReceiver)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = []


def get_device_list_by_type_ext(receiveBuffer):
    '''
    Get the contents of the device list which match the supplied typeID.

    Parameters
    ----------
        receiveBuffer: POINTER(c_char)
        sizeOfBuffer: c_ulong
        typeID: c_int

    Returns
    -------
        c_short
    '''

    receiveBuffer = POINTER(c_char)()
    sizeOfBuffer = c_ulong()
    typeID = c_int()

    output = TLI_GetDeviceListByTypeExt(receiveBuffer)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = []


def get_device_list_by_types(stringsReceiver):
    '''
    Get the contents of the device list which match the supplied typeIDs.

    Parameters
    ----------
        stringsReceiver: SafeArray
        typeIDs: c_int
        length: c_int

    Returns
    -------
        c_short
    '''

    stringsReceiver = SafeArray()
    typeIDs = c_int()
    length = c_int()

    output = TLI_GetDeviceListByTypes(stringsReceiver)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = []


def get_device_list_by_types_ext(receiveBuffer):
    '''
    Get the contents of the device list which match the supplied typeIDs.

    Parameters
    ----------
        receiveBuffer: POINTER(c_char)
        sizeOfBuffer: c_ulong
        typeIDs: c_int
        length: c_int

    Returns
    -------
        c_short
    '''

    receiveBuffer = POINTER(c_char)()
    sizeOfBuffer = c_ulong()
    typeIDs = c_int()
    length = c_int()

    output = TLI_GetDeviceListByTypesExt(receiveBuffer)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = []


def get_device_list_ext(receiveBuffer):
    '''
    Get the entire contents of the device list.

    Parameters
    ----------
        receiveBuffer: POINTER(c_char)
        sizeOfBuffer: c_ulong

    Returns
    -------
        c_short
    '''

    receiveBuffer = POINTER(c_char)()
    sizeOfBuffer = c_ulong()

    output = TLI_GetDeviceListExt(receiveBuffer)

    if output != 0:
        raise KinesisException(output)



TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short
TLI_GetDeviceListSize.argtypes = []


def get_device_list_size():
    '''
    Gets the device list size.

    Parameters
    ----------

    Returns
    -------
        c_short
    '''


    output = TLI_GetDeviceListSize()

    if output != 0:
        raise KinesisException(output)



TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p
TLI_InitializeSimulations.argtypes = []


def initialize_simulations():
    '''
    Initialize a connection to the Simulation Manager, which must already be running.

    Parameters
    ----------

    Returns
    -------
        c_void_p
    '''


    output = TLI_InitializeSimulations()

    return output



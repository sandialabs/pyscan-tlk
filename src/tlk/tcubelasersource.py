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
    LS_DisplayUnits,
    LS_InputSourceFlags)
from .definitions.structures import (
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
    lib_path + "Thorlabs.MotionControl.TCube.LaserSource.DLL")

LS_CheckConnection = lib.LS_CheckConnection
LS_CheckConnection.restype = c_bool
LS_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = LS_CheckConnection(serial_number)

    return output


LS_ClearMessageQueue = lib.LS_ClearMessageQueue
LS_ClearMessageQueue.restype = c_void_p
LS_ClearMessageQueue.argtypes = []


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

    output = LS_ClearMessageQueue(serial_number)

    return output


LS_Close = lib.LS_Close
LS_Close.restype = c_void_p
LS_Close.argtypes = []


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

    output = LS_Close(serial_number)

    return output


LS_Disable = lib.LS_Disable
LS_Disable.restype = c_short
LS_Disable.argtypes = []


def disable(serial_number):
    '''
    Disable laser.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_Disable(serial_number)

    return output


LS_DisableOutput = lib.LS_DisableOutput
LS_DisableOutput.restype = c_short
LS_DisableOutput.argtypes = []


def disable_output(serial_number):
    '''
    Switch laser off.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_DisableOutput(serial_number)

    return output


LS_Enable = lib.LS_Enable
LS_Enable.restype = c_short
LS_Enable.argtypes = []


def enable(serial_number):
    '''
    Enable laser for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_Enable(serial_number)

    return output


LS_EnableLastMsgTimer = lib.LS_EnableLastMsgTimer
LS_EnableLastMsgTimer.restype = c_void_p
LS_EnableLastMsgTimer.argtypes = []


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

    output = LS_EnableLastMsgTimer(serial_number)

    return output


LS_EnableOutput = lib.LS_EnableOutput
LS_EnableOutput.restype = c_short
LS_EnableOutput.argtypes = []


def enable_output(serial_number):
    '''
    Switch laser on.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_EnableOutput(serial_number)

    return output


LS_GetControlSource = lib.LS_GetControlSource
LS_GetControlSource.restype = LS_InputSourceFlags
LS_GetControlSource.argtypes = []


def get_control_source(serial_number):
    '''
    Gets the control input source.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        LS_InputSourceFlags
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetControlSource(serial_number)

    return output


LS_GetCurrentReading = lib.LS_GetCurrentReading
LS_GetCurrentReading.restype = c_long
LS_GetCurrentReading.argtypes = []


def get_current_reading(serial_number):
    '''
    Gets current Current reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetCurrentReading(serial_number)

    return output


LS_GetDisplayUnits = lib.LS_GetDisplayUnits
LS_GetDisplayUnits.restype = LS_DisplayUnits
LS_GetDisplayUnits.argtypes = []


def get_display_units(serial_number):
    '''
    Gets the hardware display units.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        LS_DisplayUnits
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetDisplayUnits(serial_number)

    return output


LS_GetFirmwareVersion = lib.LS_GetFirmwareVersion
LS_GetFirmwareVersion.restype = c_ulong
LS_GetFirmwareVersion.argtypes = []


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

    output = LS_GetFirmwareVersion(serial_number)

    return output


LS_GetHardwareInfo = lib.LS_GetHardwareInfo
LS_GetHardwareInfo.restype = c_short
LS_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = LS_GetHardwareInfo(serial_number)

    return output


LS_GetHardwareInfoBlock = lib.LS_GetHardwareInfoBlock
LS_GetHardwareInfoBlock.restype = c_short
LS_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = LS_GetHardwareInfoBlock(serial_number)

    return output


LS_GetInterlockState = lib.LS_GetInterlockState
LS_GetInterlockState.restype = c_byte
LS_GetInterlockState.argtypes = []


def get_interlock_state(serial_number):
    '''
    Gets the Interlock State.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetInterlockState(serial_number)

    return output


LS_GetLEDBrightness = lib.LS_GetLEDBrightness
LS_GetLEDBrightness.restype = c_long
LS_GetLEDBrightness.argtypes = []


def get_l_e_d_brightness(serial_number):
    '''
    Gets the LED brightness.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetLEDBrightness(serial_number)

    return output


LS_GetLimits = lib.LS_GetLimits
LS_GetLimits.restype = c_short
LS_GetLimits.argtypes = []


def get_limits(serial_number):
    '''
    Gets the max power and current limits for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        maxPower: c_long
        maxCurrent: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    maxPower = c_long()
    maxCurrent = c_long()

    output = LS_GetLimits(serial_number)

    return output


LS_GetNextMessage = lib.LS_GetNextMessage
LS_GetNextMessage.restype = c_bool
LS_GetNextMessage.argtypes = []


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

    output = LS_GetNextMessage(serial_number)

    return output


LS_GetPowerReading = lib.LS_GetPowerReading
LS_GetPowerReading.restype = c_long
LS_GetPowerReading.argtypes = []


def get_power_reading(serial_number):
    '''
    Gets current power reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetPowerReading(serial_number)

    return output


LS_GetPowerSet = lib.LS_GetPowerSet
LS_GetPowerSet.restype = c_long
LS_GetPowerSet.argtypes = []


def get_power_set(serial_number):
    '''
    Gets the output power currently set.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetPowerSet(serial_number)

    return output


LS_GetSoftwareVersion = lib.LS_GetSoftwareVersion
LS_GetSoftwareVersion.restype = c_ulong
LS_GetSoftwareVersion.argtypes = []


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

    output = LS_GetSoftwareVersion(serial_number)

    return output


LS_GetStatusBits = lib.LS_GetStatusBits
LS_GetStatusBits.restype = c_ulong
LS_GetStatusBits.argtypes = []


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

    output = LS_GetStatusBits(serial_number)

    return output


LS_GetWavelength = lib.LS_GetWavelength
LS_GetWavelength.restype = c_long
LS_GetWavelength.argtypes = []


def get_wavelength(serial_number):
    '''
    Gets the operating wavelength.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_GetWavelength(serial_number)

    return output


LS_HasLastMsgTimerOverrun = lib.LS_HasLastMsgTimerOverrun
LS_HasLastMsgTimerOverrun.restype = c_bool
LS_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by LS_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_HasLastMsgTimerOverrun(serial_number)

    return output


LS_Identify = lib.LS_Identify
LS_Identify.restype = c_void_p
LS_Identify.argtypes = []


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

    output = LS_Identify(serial_number)

    return output


LS_LoadNamedSettings = lib.LS_LoadNamedSettings
LS_LoadNamedSettings.restype = c_bool
LS_LoadNamedSettings.argtypes = []


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

    output = LS_LoadNamedSettings(serial_number)

    return output


LS_LoadSettings = lib.LS_LoadSettings
LS_LoadSettings.restype = c_bool
LS_LoadSettings.argtypes = []


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

    output = LS_LoadSettings(serial_number)

    return output


LS_MessageQueueSize = lib.LS_MessageQueueSize
LS_MessageQueueSize.restype = c_int
LS_MessageQueueSize.argtypes = []


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

    output = LS_MessageQueueSize(serial_number)

    return output


LS_Open = lib.LS_Open
LS_Open.restype = c_short
LS_Open.argtypes = []


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

    output = LS_Open(serial_number)

    return output


LS_PersistSettings = lib.LS_PersistSettings
LS_PersistSettings.restype = c_bool
LS_PersistSettings.argtypes = []


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

    output = LS_PersistSettings(serial_number)

    return output


LS_PollingDuration = lib.LS_PollingDuration
LS_PollingDuration.restype = c_long
LS_PollingDuration.argtypes = []


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

    output = LS_PollingDuration(serial_number)

    return output


LS_RegisterMessageCallback = lib.LS_RegisterMessageCallback
LS_RegisterMessageCallback.restype = c_void_p
LS_RegisterMessageCallback.argtypes = []


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

    output = LS_RegisterMessageCallback(serial_number)

    return output


LS_RequestControlSource = lib.LS_RequestControlSource
LS_RequestControlSource.restype = c_short
LS_RequestControlSource.argtypes = []


def request_control_source(serial_number):
    '''
    Gets the control input source.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestControlSource(serial_number)

    return output


LS_RequestDisplayUnits = lib.LS_RequestDisplayUnits
LS_RequestDisplayUnits.restype = c_short
LS_RequestDisplayUnits.argtypes = []


def request_display_units(serial_number):
    '''
    Requests the hardware display units.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestDisplayUnits(serial_number)

    return output


LS_RequestLEDBrightness = lib.LS_RequestLEDBrightness
LS_RequestLEDBrightness.restype = c_short
LS_RequestLEDBrightness.argtypes = []


def request_l_e_d_brightness(serial_number):
    '''
    Requests the LED Brightness.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestLEDBrightness(serial_number)

    return output


LS_RequestLimits = lib.LS_RequestLimits
LS_RequestLimits.restype = c_short
LS_RequestLimits.argtypes = []


def request_limits(serial_number):
    '''
    Requests the limits MaxPower and MaxCurrent.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestLimits(serial_number)

    return output


LS_RequestReadings = lib.LS_RequestReadings
LS_RequestReadings.restype = c_short
LS_RequestReadings.argtypes = []


def request_readings(serial_number):
    '''
    Request power and current readings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestReadings(serial_number)

    return output


LS_RequestSetPower = lib.LS_RequestSetPower
LS_RequestSetPower.restype = c_short
LS_RequestSetPower.argtypes = []


def request_set_power(serial_number):
    '''
    Sets the output power.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestSetPower(serial_number)

    return output


LS_RequestSettings = lib.LS_RequestSettings
LS_RequestSettings.restype = c_short
LS_RequestSettings.argtypes = []


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

    output = LS_RequestSettings(serial_number)

    return output


LS_RequestStatus = lib.LS_RequestStatus
LS_RequestStatus.restype = c_short
LS_RequestStatus.argtypes = []


def request_status(serial_number):
    '''
    Requests the state quantities (actual power, current and status).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestStatus(serial_number)

    return output


LS_RequestStatusBits = lib.LS_RequestStatusBits
LS_RequestStatusBits.restype = c_short
LS_RequestStatusBits.argtypes = []


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

    output = LS_RequestStatusBits(serial_number)

    return output


LS_RequestWavelength = lib.LS_RequestWavelength
LS_RequestWavelength.restype = c_short
LS_RequestWavelength.argtypes = []


def request_wavelength(serial_number):
    '''
    Requests the device Wavelength.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LS_RequestWavelength(serial_number)

    return output


LS_SetControlSource = lib.LS_SetControlSource
LS_SetControlSource.restype = c_short
LS_SetControlSource.argtypes = []


def set_control_source(serial_number):
    '''
    Sets the control input source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        source: LS_InputSourceFlags

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    source = LS_InputSourceFlags()

    output = LS_SetControlSource(serial_number)

    return output


LS_SetDisplayUnits = lib.LS_SetDisplayUnits
LS_SetDisplayUnits.restype = c_short
LS_SetDisplayUnits.argtypes = []


def set_display_units(serial_number):
    '''
    Sets the hardware display units.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        units: LS_DisplayUnits

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    units = LS_DisplayUnits()

    output = LS_SetDisplayUnits(serial_number)

    return output


LS_SetLEDBrightness = lib.LS_SetLEDBrightness
LS_SetLEDBrightness.restype = c_short
LS_SetLEDBrightness.argtypes = []


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

    output = LS_SetLEDBrightness(serial_number)

    return output


LS_SetPower = lib.LS_SetPower
LS_SetPower.restype = c_short
LS_SetPower.argtypes = []


def set_power(serial_number):
    '''
    Sets the output power.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        power: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    power = c_long()

    output = LS_SetPower(serial_number)

    return output


LS_StartPolling = lib.LS_StartPolling
LS_StartPolling.restype = c_bool
LS_StartPolling.argtypes = []


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

    output = LS_StartPolling(serial_number)

    return output


LS_StopPolling = lib.LS_StopPolling
LS_StopPolling.restype = c_void_p
LS_StopPolling.argtypes = []


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

    output = LS_StopPolling(serial_number)

    return output


LS_TimeSinceLastMsgReceived = lib.LS_TimeSinceLastMsgReceived
LS_TimeSinceLastMsgReceived.restype = c_bool
LS_TimeSinceLastMsgReceived.argtypes = []


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

    output = LS_TimeSinceLastMsgReceived(serial_number)

    return output


LS_WaitForMessage = lib.LS_WaitForMessage
LS_WaitForMessage.restype = c_bool
LS_WaitForMessage.argtypes = []


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

    output = LS_WaitForMessage(serial_number)

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



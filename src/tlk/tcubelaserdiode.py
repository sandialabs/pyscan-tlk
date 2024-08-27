from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_char_p,
    c_float,
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
    LD_DisplayUnits,
    LD_InputSourceFlags,
    LD_POLARITY)
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
    lib_path + "Thorlabs.MotionControl.TCube.LaserDiode.DLL")

LD_CheckConnection = lib.LD_CheckConnection
LD_CheckConnection.restype = c_bool
LD_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = LD_CheckConnection(serial_number)

    return output


LD_ClearMessageQueue = lib.LD_ClearMessageQueue
LD_ClearMessageQueue.restype = c_void_p
LD_ClearMessageQueue.argtypes = []


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

    output = LD_ClearMessageQueue(serial_number)

    return output


LD_Close = lib.LD_Close
LD_Close.restype = c_void_p
LD_Close.argtypes = []


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

    output = LD_Close(serial_number)

    return output


LD_Disable = lib.LD_Disable
LD_Disable.restype = c_short
LD_Disable.argtypes = []


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

    output = LD_Disable(serial_number)

    return output


LD_DisableOutput = lib.LD_DisableOutput
LD_DisableOutput.restype = c_short
LD_DisableOutput.argtypes = []


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

    output = LD_DisableOutput(serial_number)

    return output


LD_Enable = lib.LD_Enable
LD_Enable.restype = c_short
LD_Enable.argtypes = []


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

    output = LD_Enable(serial_number)

    return output


LD_EnableLastMsgTimer = lib.LD_EnableLastMsgTimer
LD_EnableLastMsgTimer.restype = c_void_p
LD_EnableLastMsgTimer.argtypes = []


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

    output = LD_EnableLastMsgTimer(serial_number)

    return output


LD_EnableMaxCurrentAdjust = lib.LD_EnableMaxCurrentAdjust
LD_EnableMaxCurrentAdjust.restype = c_short
LD_EnableMaxCurrentAdjust.argtypes = []


def enable_max_current_adjust(serial_number):
    '''
    Enables the maximum current adjust mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        enableAdjust: c_bool
        enableDiode: c_bool

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    enableAdjust = c_bool()
    enableDiode = c_bool()

    output = LD_EnableMaxCurrentAdjust(serial_number)

    return output


LD_EnableOutput = lib.LD_EnableOutput
LD_EnableOutput.restype = c_short
LD_EnableOutput.argtypes = []


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

    output = LD_EnableOutput(serial_number)

    return output


LD_EnableTIAGainAdjust = lib.LD_EnableTIAGainAdjust
LD_EnableTIAGainAdjust.restype = c_short
LD_EnableTIAGainAdjust.argtypes = []


def enable_t_i_a_gain_adjust(serial_number):
    '''
    Enables the tia gain adjustment mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        enable: c_bool

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    enable = c_bool()

    output = LD_EnableTIAGainAdjust(serial_number)

    return output


LD_FindTIAGain = lib.LD_FindTIAGain
LD_FindTIAGain.restype = c_short
LD_FindTIAGain.argtypes = []


def find_t_i_a_gain(serial_number):
    '''
    Performs the FindTIAGain calibration.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_FindTIAGain(serial_number)

    return output


LD_GetControlSource = lib.LD_GetControlSource
LD_GetControlSource.restype = LD_InputSourceFlags
LD_GetControlSource.argtypes = []


def get_control_source(serial_number):
    '''
    Gets the control input source.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        LD_InputSourceFlags
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetControlSource(serial_number)

    return output


LD_GetDisplayUnits = lib.LD_GetDisplayUnits
LD_GetDisplayUnits.restype = LD_DisplayUnits
LD_GetDisplayUnits.argtypes = []


def get_display_units(serial_number):
    '''
    Gets the hardware display units.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        LD_DisplayUnits
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetDisplayUnits(serial_number)

    return output


LD_GetFirmwareVersion = lib.LD_GetFirmwareVersion
LD_GetFirmwareVersion.restype = c_ulong
LD_GetFirmwareVersion.argtypes = []


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

    output = LD_GetFirmwareVersion(serial_number)

    return output


LD_GetHardwareInfo = lib.LD_GetHardwareInfo
LD_GetHardwareInfo.restype = c_short
LD_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = LD_GetHardwareInfo(serial_number)

    return output


LD_GetHardwareInfoBlock = lib.LD_GetHardwareInfoBlock
LD_GetHardwareInfoBlock.restype = c_short
LD_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = LD_GetHardwareInfoBlock(serial_number)

    return output


LD_GetInterlockState = lib.LD_GetInterlockState
LD_GetInterlockState.restype = c_byte
LD_GetInterlockState.argtypes = []


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

    output = LD_GetInterlockState(serial_number)

    return output


LD_GetLEDBrightness = lib.LD_GetLEDBrightness
LD_GetLEDBrightness.restype = c_long
LD_GetLEDBrightness.argtypes = []


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

    output = LD_GetLEDBrightness(serial_number)

    return output


LD_GetLaserDiodeCurrentReading = lib.LD_GetLaserDiodeCurrentReading
LD_GetLaserDiodeCurrentReading.restype = c_long
LD_GetLaserDiodeCurrentReading.argtypes = []


def get_laser_diode_current_reading(serial_number):
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

    output = LD_GetLaserDiodeCurrentReading(serial_number)

    return output


LD_GetLaserDiodeMaxCurrentLimit = lib.LD_GetLaserDiodeMaxCurrentLimit
LD_GetLaserDiodeMaxCurrentLimit.restype = c_long
LD_GetLaserDiodeMaxCurrentLimit.argtypes = []


def get_laser_diode_max_current_limit(serial_number):
    '''
    Gets the Laser Diode max current limit.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetLaserDiodeMaxCurrentLimit(serial_number)

    return output


LD_GetLaserPolarity = lib.LD_GetLaserPolarity
LD_GetLaserPolarity.restype = LD_POLARITY
LD_GetLaserPolarity.argtypes = []


def get_laser_polarity(serial_number):
    '''
    Gets the laser polarity.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        LD_POLARITY
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetLaserPolarity(serial_number)

    return output


LD_GetLaserSetPoint = lib.LD_GetLaserSetPoint
LD_GetLaserSetPoint.restype = c_long
LD_GetLaserSetPoint.argtypes = []


def get_laser_set_point(serial_number):
    '''
    Gets the Laser Diode Current currently set.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetLaserSetPoint(serial_number)

    return output


LD_GetMaxCurrentDigPot = lib.LD_GetMaxCurrentDigPot
LD_GetMaxCurrentDigPot.restype = c_long
LD_GetMaxCurrentDigPot.argtypes = []


def get_max_current_dig_pot(serial_number):
    '''
    Gets the maximum current dig pot position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetMaxCurrentDigPot(serial_number)

    return output


LD_GetNextMessage = lib.LD_GetNextMessage
LD_GetNextMessage.restype = c_bool
LD_GetNextMessage.argtypes = []


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

    output = LD_GetNextMessage(serial_number)

    return output


LD_GetPhotoCurrentReading = lib.LD_GetPhotoCurrentReading
LD_GetPhotoCurrentReading.restype = c_long
LD_GetPhotoCurrentReading.argtypes = []


def get_photo_current_reading(serial_number):
    '''
    Gets current Photo Current reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetPhotoCurrentReading(serial_number)

    return output


LD_GetSoftwareVersion = lib.LD_GetSoftwareVersion
LD_GetSoftwareVersion.restype = c_ulong
LD_GetSoftwareVersion.argtypes = []


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

    output = LD_GetSoftwareVersion(serial_number)

    return output


LD_GetStatusBits = lib.LD_GetStatusBits
LD_GetStatusBits.restype = c_ulong
LD_GetStatusBits.argtypes = []


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

    output = LD_GetStatusBits(serial_number)

    return output


LD_GetVoltageReading = lib.LD_GetVoltageReading
LD_GetVoltageReading.restype = c_long
LD_GetVoltageReading.argtypes = []


def get_voltage_reading(serial_number):
    '''
    Gets current Voltage reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetVoltageReading(serial_number)

    return output


LD_GetWACalibFactor = lib.LD_GetWACalibFactor
LD_GetWACalibFactor.restype = c_float
LD_GetWACalibFactor.argtypes = []


def get_w_a_calib_factor(serial_number):
    '''
    Gets the W/A calibration factor.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_float
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_GetWACalibFactor(serial_number)

    return output


LD_HasLastMsgTimerOverrun = lib.LD_HasLastMsgTimerOverrun
LD_HasLastMsgTimerOverrun.restype = c_bool
LD_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by LD_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_HasLastMsgTimerOverrun(serial_number)

    return output


LD_Identify = lib.LD_Identify
LD_Identify.restype = c_void_p
LD_Identify.argtypes = []


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

    output = LD_Identify(serial_number)

    return output


LD_LoadNamedSettings = lib.LD_LoadNamedSettings
LD_LoadNamedSettings.restype = c_bool
LD_LoadNamedSettings.argtypes = []


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

    output = LD_LoadNamedSettings(serial_number)

    return output


LD_LoadSettings = lib.LD_LoadSettings
LD_LoadSettings.restype = c_bool
LD_LoadSettings.argtypes = []


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

    output = LD_LoadSettings(serial_number)

    return output


LD_MessageQueueSize = lib.LD_MessageQueueSize
LD_MessageQueueSize.restype = c_int
LD_MessageQueueSize.argtypes = []


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

    output = LD_MessageQueueSize(serial_number)

    return output


LD_Open = lib.LD_Open
LD_Open.restype = c_short
LD_Open.argtypes = []


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

    output = LD_Open(serial_number)

    return output


LD_PersistSettings = lib.LD_PersistSettings
LD_PersistSettings.restype = c_bool
LD_PersistSettings.argtypes = []


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

    output = LD_PersistSettings(serial_number)

    return output


LD_PollingDuration = lib.LD_PollingDuration
LD_PollingDuration.restype = c_long
LD_PollingDuration.argtypes = []


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

    output = LD_PollingDuration(serial_number)

    return output


LD_RegisterMessageCallback = lib.LD_RegisterMessageCallback
LD_RegisterMessageCallback.restype = c_void_p
LD_RegisterMessageCallback.argtypes = []


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

    output = LD_RegisterMessageCallback(serial_number)

    return output


LD_RequestControlSource = lib.LD_RequestControlSource
LD_RequestControlSource.restype = c_short
LD_RequestControlSource.argtypes = []


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

    output = LD_RequestControlSource(serial_number)

    return output


LD_RequestDisplay = lib.LD_RequestDisplay
LD_RequestDisplay.restype = c_short
LD_RequestDisplay.argtypes = []


def request_display(serial_number):
    '''
    Requests the display parameters (Units and Intensity).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_RequestDisplay(serial_number)

    return output


LD_RequestLaserDiodeMaxCurrentLimit = lib.LD_RequestLaserDiodeMaxCurrentLimit
LD_RequestLaserDiodeMaxCurrentLimit.restype = c_short
LD_RequestLaserDiodeMaxCurrentLimit.argtypes = []


def request_laser_diode_max_current_limit(serial_number):
    '''
    Requests the Laser Diode max current limit.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_RequestLaserDiodeMaxCurrentLimit(serial_number)

    return output


LD_RequestLaserPolarity = lib.LD_RequestLaserPolarity
LD_RequestLaserPolarity.restype = c_short
LD_RequestLaserPolarity.argtypes = []


def request_laser_polarity(serial_number):
    '''
    Requests the laser polarity.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_RequestLaserPolarity(serial_number)

    return output


LD_RequestLaserSetPoint = lib.LD_RequestLaserSetPoint
LD_RequestLaserSetPoint.restype = c_short
LD_RequestLaserSetPoint.argtypes = []


def request_laser_set_point(serial_number):
    '''
    Sets the output point (power / current / voltage).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_RequestLaserSetPoint(serial_number)

    return output


LD_RequestMaxCurrentDigPot = lib.LD_RequestMaxCurrentDigPot
LD_RequestMaxCurrentDigPot.restype = c_short
LD_RequestMaxCurrentDigPot.argtypes = []


def request_max_current_dig_pot(serial_number):
    '''
    requests the maximum current dig pot position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_RequestMaxCurrentDigPot(serial_number)

    return output


LD_RequestReadings = lib.LD_RequestReadings
LD_RequestReadings.restype = c_short
LD_RequestReadings.argtypes = []


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

    output = LD_RequestReadings(serial_number)

    return output


LD_RequestSettings = lib.LD_RequestSettings
LD_RequestSettings.restype = c_short
LD_RequestSettings.argtypes = []


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

    output = LD_RequestSettings(serial_number)

    return output


LD_RequestStatus = lib.LD_RequestStatus
LD_RequestStatus.restype = c_short
LD_RequestStatus.argtypes = []


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

    output = LD_RequestStatus(serial_number)

    return output


LD_RequestStatusBits = lib.LD_RequestStatusBits
LD_RequestStatusBits.restype = c_short
LD_RequestStatusBits.argtypes = []


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

    output = LD_RequestStatusBits(serial_number)

    return output


LD_RequestWACalibFactor = lib.LD_RequestWACalibFactor
LD_RequestWACalibFactor.restype = c_short
LD_RequestWACalibFactor.argtypes = []


def request_w_a_calib_factor(serial_number):
    '''
    Requests the wa calib factor.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_RequestWACalibFactor(serial_number)

    return output


LD_SetClosedLoopMode = lib.LD_SetClosedLoopMode
LD_SetClosedLoopMode.restype = c_short
LD_SetClosedLoopMode.argtypes = []


def set_closed_loop_mode(serial_number):
    '''
    Set closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_SetClosedLoopMode(serial_number)

    return output


LD_SetControlSource = lib.LD_SetControlSource
LD_SetControlSource.restype = c_short
LD_SetControlSource.argtypes = []


def set_control_source(serial_number):
    '''
    Sets the control input source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        source: LD_InputSourceFlags

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    source = LD_InputSourceFlags()

    output = LD_SetControlSource(serial_number)

    return output


LD_SetDisplayUnits = lib.LD_SetDisplayUnits
LD_SetDisplayUnits.restype = c_short
LD_SetDisplayUnits.argtypes = []


def set_display_units(serial_number):
    '''
    Sets the hardware display units.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        units: LD_DisplayUnits

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    units = LD_DisplayUnits()

    output = LD_SetDisplayUnits(serial_number)

    return output


LD_SetLEDBrightness = lib.LD_SetLEDBrightness
LD_SetLEDBrightness.restype = c_short
LD_SetLEDBrightness.argtypes = []


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

    output = LD_SetLEDBrightness(serial_number)

    return output


LD_SetLaserPolarity = lib.LD_SetLaserPolarity
LD_SetLaserPolarity.restype = c_short
LD_SetLaserPolarity.argtypes = []


def set_laser_polarity(serial_number):
    '''
    Sets the laser polarity.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        polarity: LD_POLARITY

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    polarity = LD_POLARITY()

    output = LD_SetLaserPolarity(serial_number)

    return output


LD_SetLaserSetPoint = lib.LD_SetLaserSetPoint
LD_SetLaserSetPoint.restype = c_short
LD_SetLaserSetPoint.argtypes = []


def set_laser_set_point(serial_number):
    '''
    Sets the Laser Diode Current.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        laserDiodeCurrent: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    laserDiodeCurrent = c_long()

    output = LD_SetLaserSetPoint(serial_number)

    return output


LD_SetMaxCurrentDigPot = lib.LD_SetMaxCurrentDigPot
LD_SetMaxCurrentDigPot.restype = c_short
LD_SetMaxCurrentDigPot.argtypes = []


def set_max_current_dig_pot(serial_number):
    '''
    Sets the maximum current digital pot position.

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

    output = LD_SetMaxCurrentDigPot(serial_number)

    return output


LD_SetOpenLoopMode = lib.LD_SetOpenLoopMode
LD_SetOpenLoopMode.restype = c_short
LD_SetOpenLoopMode.argtypes = []


def set_open_loop_mode(serial_number):
    '''
    Set open loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = LD_SetOpenLoopMode(serial_number)

    return output


LD_SetWACalibFactor = lib.LD_SetWACalibFactor
LD_SetWACalibFactor.restype = c_short
LD_SetWACalibFactor.argtypes = []


def set_w_a_calib_factor(serial_number):
    '''
    Sets the W/A calibration factor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        calibFactor: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    calibFactor = c_float()

    output = LD_SetWACalibFactor(serial_number)

    return output


LD_StartPolling = lib.LD_StartPolling
LD_StartPolling.restype = c_bool
LD_StartPolling.argtypes = []


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

    output = LD_StartPolling(serial_number)

    return output


LD_StopPolling = lib.LD_StopPolling
LD_StopPolling.restype = c_void_p
LD_StopPolling.argtypes = []


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

    output = LD_StopPolling(serial_number)

    return output


LD_TimeSinceLastMsgReceived = lib.LD_TimeSinceLastMsgReceived
LD_TimeSinceLastMsgReceived.restype = c_bool
LD_TimeSinceLastMsgReceived.argtypes = []


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

    output = LD_TimeSinceLastMsgReceived(serial_number)

    return output


LD_WaitForMessage = lib.LD_WaitForMessage
LD_WaitForMessage.restype = c_bool
LD_WaitForMessage.argtypes = []


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

    output = LD_WaitForMessage(serial_number)

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



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
    QD_OperatingMode)
from .definitions.structures import (
    QD_ClosedLoopPosition,
    QD_KPA_DigitalIO,
    QD_KPA_TrigIOConfig,
    QD_LoopParameters,
    QD_LowPassFilterParameters,
    QD_NotchFilterParameters,
    QD_PIDParameters,
    QD_Position,
    QD_PositionDemandParameters,
    QD_Readings,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.PositionAligner.DLL")

QD_CanDeviceLockFrontPanel = lib.QD_CanDeviceLockFrontPanel
QD_CanDeviceLockFrontPanel.restype = c_bool
QD_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    '''
    Determine if the device front panel can be locked.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_CanDeviceLockFrontPanel(serial_number)

    return output


QD_CheckConnection = lib.QD_CheckConnection
QD_CheckConnection.restype = c_bool
QD_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    '''
    Check connection.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_CheckConnection(serial_number)

    return output


QD_ClearMessageQueue = lib.QD_ClearMessageQueue
QD_ClearMessageQueue.restype = c_void_p
QD_ClearMessageQueue.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_ClearMessageQueue(serial_number)

    return output


QD_Close = lib.QD_Close
QD_Close.restype = c_void_p
QD_Close.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_Close(serial_number)

    return output


QD_EnableLastMsgTimer = lib.QD_EnableLastMsgTimer
QD_EnableLastMsgTimer.restype = c_void_p
QD_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = QD_EnableLastMsgTimer(serial_number)

    return output


QD_GetClosedLoopPosition = lib.QD_GetClosedLoopPosition
QD_GetClosedLoopPosition.restype = c_short
QD_GetClosedLoopPosition.argtypes = [POINTER(c_char)]


def get_closed_loop_position(serial_number):
    '''
    Gets closed loop position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: QD_ClosedLoopPosition

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = QD_ClosedLoopPosition()

    output = QD_GetClosedLoopPosition(serial_number)

    return output


QD_GetDemandedPosition = lib.QD_GetDemandedPosition
QD_GetDemandedPosition.restype = c_short
QD_GetDemandedPosition.argtypes = [POINTER(c_char)]


def get_demanded_position(serial_number):
    '''
    Gets position demand output.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: QD_Position

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = QD_Position()

    output = QD_GetDemandedPosition(serial_number)

    return output


QD_GetDigitalOutput = lib.QD_GetDigitalOutput
QD_GetDigitalOutput.restype = c_short
QD_GetDigitalOutput.argtypes = [POINTER(c_char)]


def get_digital_output(serial_number):
    '''
    Sets the digital IO parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        digitalIO: QD_KPA_DigitalIO

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    digitalIO = QD_KPA_DigitalIO()

    output = QD_GetDigitalOutput(serial_number)

    return output


QD_GetFirmwareVersion = lib.QD_GetFirmwareVersion
QD_GetFirmwareVersion.restype = c_ulong
QD_GetFirmwareVersion.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_GetFirmwareVersion(serial_number)

    return output


QD_GetFrontPanelLocked = lib.QD_GetFrontPanelLocked
QD_GetFrontPanelLocked.restype = c_bool
QD_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    '''
    Query if the device front panel locked.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_GetFrontPanelLocked(serial_number)

    return output


QD_GetHardwareInfo = lib.QD_GetHardwareInfo
QD_GetHardwareInfo.restype = c_short
QD_GetHardwareInfo.argtypes = [POINTER(c_char)]


def get_hardware_info(serial_number):
    '''
    Gets the hardware information from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        modelNo: POINTER(c_char)
        sizeOfModelNo: c_ulong
        type: c_long
        numChannels: c_long
        notes: POINTER(c_char)
        sizeOfNotes: c_ulong
        firmwareVersion: c_ulong
        hardwareVersion: c_long
        modificationState: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = QD_GetHardwareInfo(serial_number)

    return output


QD_GetHardwareInfoBlock = lib.QD_GetHardwareInfoBlock
QD_GetHardwareInfoBlock.restype = c_short
QD_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


def get_hardware_info_block(serial_number):
    '''
    Gets the hardware information in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        hardwareInfo: TLI_HardwareInformation

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    hardwareInfo = TLI_HardwareInformation()

    output = QD_GetHardwareInfoBlock(serial_number)

    return output


QD_GetLEDBrightness = lib.QD_GetLEDBrightness
QD_GetLEDBrightness.restype = c_long
QD_GetLEDBrightness.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_GetLEDBrightness(serial_number)

    return output


QD_GetLoopPIDparams = lib.QD_GetLoopPIDparams
QD_GetLoopPIDparams.restype = c_short
QD_GetLoopPIDparams.argtypes = [POINTER(c_char)]


def get_loop_p_i_dparams(serial_number):
    '''
    Gets the feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        loopParams: QD_LoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    loopParams = QD_LoopParameters()

    output = QD_GetLoopPIDparams(serial_number)

    return output


QD_GetLowPassFilterparams = lib.QD_GetLowPassFilterparams
QD_GetLowPassFilterparams.restype = c_short
QD_GetLowPassFilterparams.argtypes = [POINTER(c_char)]


def get_low_pass_filterparams(serial_number):
    '''
    Gets the low pass filter parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        lowPassParams: QD_LowPassFilterParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    lowPassParams = QD_LowPassFilterParameters()

    output = QD_GetLowPassFilterparams(serial_number)

    return output


QD_GetNextMessage = lib.QD_GetNextMessage
QD_GetNextMessage.restype = c_bool
QD_GetNextMessage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = QD_GetNextMessage(serial_number)

    return output


QD_GetNotchFilterparams = lib.QD_GetNotchFilterparams
QD_GetNotchFilterparams.restype = c_short
QD_GetNotchFilterparams.argtypes = [POINTER(c_char)]


def get_notch_filterparams(serial_number):
    '''
    Gets the notch filter parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        notchParams: QD_NotchFilterParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    notchParams = QD_NotchFilterParameters()

    output = QD_GetNotchFilterparams(serial_number)

    return output


QD_GetOperatingMode = lib.QD_GetOperatingMode
QD_GetOperatingMode.restype = QD_OperatingMode
QD_GetOperatingMode.argtypes = [POINTER(c_char)]


def get_operating_mode(serial_number):
    '''
    Gets the operating mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        QD_OperatingMode
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_GetOperatingMode(serial_number)

    return output


QD_GetPIDparams = lib.QD_GetPIDparams
QD_GetPIDparams.restype = c_short
QD_GetPIDparams.argtypes = [POINTER(c_char)]


def get_p_i_dparams(serial_number):
    '''
    Gets the feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalIntegralDerivativeParams: QD_PIDParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalIntegralDerivativeParams = QD_PIDParameters()

    output = QD_GetPIDparams(serial_number)

    return output


QD_GetPosDemandParams = lib.QD_GetPosDemandParams
QD_GetPosDemandParams.restype = c_short
QD_GetPosDemandParams.argtypes = [POINTER(c_char)]


def get_pos_demand_params(serial_number):
    '''
    Gets the position demand output parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        demandParams: QD_PositionDemandParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    demandParams = QD_PositionDemandParameters()

    output = QD_GetPosDemandParams(serial_number)

    return output


QD_GetReading = lib.QD_GetReading
QD_GetReading.restype = c_short
QD_GetReading.argtypes = [POINTER(c_char)]


def get_reading(serial_number):
    '''
    Gets a reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        reading: QD_Readings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    reading = QD_Readings()

    output = QD_GetReading(serial_number)

    return output


QD_GetSoftwareVersion = lib.QD_GetSoftwareVersion
QD_GetSoftwareVersion.restype = c_ulong
QD_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_GetSoftwareVersion(serial_number)

    return output


QD_GetStatusBits = lib.QD_GetStatusBits
QD_GetStatusBits.restype = c_ulong
QD_GetStatusBits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_GetStatusBits(serial_number)

    return output


QD_GetTriggerConfigParams = lib.QD_GetTriggerConfigParams
QD_GetTriggerConfigParams.restype = c_short
QD_GetTriggerConfigParams.argtypes = [POINTER(c_char)]


def get_trigger_config_params(serial_number):
    '''
    Gets the trigger config parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerParams: QD_KPA_TrigIOConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerParams = QD_KPA_TrigIOConfig()

    output = QD_GetTriggerConfigParams(serial_number)

    return output


QD_HasLastMsgTimerOverrun = lib.QD_HasLastMsgTimerOverrun
QD_HasLastMsgTimerOverrun.restype = c_bool
QD_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by QD_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_HasLastMsgTimerOverrun(serial_number)

    return output


QD_Identify = lib.QD_Identify
QD_Identify.restype = c_void_p
QD_Identify.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_Identify(serial_number)

    return output


QD_LoadNamedSettings = lib.QD_LoadNamedSettings
QD_LoadNamedSettings.restype = c_bool
QD_LoadNamedSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    settingsName = POINTER(c_char)()

    output = QD_LoadNamedSettings(serial_number)

    return output


QD_LoadSettings = lib.QD_LoadSettings
QD_LoadSettings.restype = c_bool
QD_LoadSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_LoadSettings(serial_number)

    return output


QD_MessageQueueSize = lib.QD_MessageQueueSize
QD_MessageQueueSize.restype = c_int
QD_MessageQueueSize.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_MessageQueueSize(serial_number)

    return output


QD_Open = lib.QD_Open
QD_Open.restype = c_short
QD_Open.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_Open(serial_number)

    return output


QD_PersistSettings = lib.QD_PersistSettings
QD_PersistSettings.restype = c_bool
QD_PersistSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_PersistSettings(serial_number)

    return output


QD_PollingDuration = lib.QD_PollingDuration
QD_PollingDuration.restype = c_long
QD_PollingDuration.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_PollingDuration(serial_number)

    return output


QD_RegisterMessageCallback = lib.QD_RegisterMessageCallback
QD_RegisterMessageCallback.restype = c_void_p
QD_RegisterMessageCallback.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RegisterMessageCallback(serial_number)

    return output


QD_RequestClosedLoopPosition = lib.QD_RequestClosedLoopPosition
QD_RequestClosedLoopPosition.restype = c_short
QD_RequestClosedLoopPosition.argtypes = [POINTER(c_char)]


def request_closed_loop_position(serial_number):
    '''
    Request the closed loop position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestClosedLoopPosition(serial_number)

    return output


QD_RequestDigitalOutput = lib.QD_RequestDigitalOutput
QD_RequestDigitalOutput.restype = c_short
QD_RequestDigitalOutput.argtypes = [POINTER(c_char)]


def request_digital_output(serial_number):
    '''
    Requests the digital IO parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestDigitalOutput(serial_number)

    return output


QD_RequestFrontPanelLocked = lib.QD_RequestFrontPanelLocked
QD_RequestFrontPanelLocked.restype = c_short
QD_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    '''
    Ask the device if its front panel is locked.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestFrontPanelLocked(serial_number)

    return output


QD_RequestLEDBrightness = lib.QD_RequestLEDBrightness
QD_RequestLEDBrightness.restype = c_short
QD_RequestLEDBrightness.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestLEDBrightness(serial_number)

    return output


QD_RequestLoopPIDparams = lib.QD_RequestLoopPIDparams
QD_RequestLoopPIDparams.restype = c_short
QD_RequestLoopPIDparams.argtypes = [POINTER(c_char)]


def request_loop_p_i_dparams(serial_number):
    '''
    Requests the feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestLoopPIDparams(serial_number)

    return output


QD_RequestOperatingMode = lib.QD_RequestOperatingMode
QD_RequestOperatingMode.restype = c_short
QD_RequestOperatingMode.argtypes = [POINTER(c_char)]


def request_operating_mode(serial_number):
    '''
    Requests the operating mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestOperatingMode(serial_number)

    return output


QD_RequestPosDemandParams = lib.QD_RequestPosDemandParams
QD_RequestPosDemandParams.restype = c_short
QD_RequestPosDemandParams.argtypes = [POINTER(c_char)]


def request_pos_demand_params(serial_number):
    '''
    Requests the position demand output parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestPosDemandParams(serial_number)

    return output


QD_RequestReading = lib.QD_RequestReading
QD_RequestReading.restype = c_short
QD_RequestReading.argtypes = [POINTER(c_char)]


def request_reading(serial_number):
    '''
    Request reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestReading(serial_number)

    return output


QD_RequestSettings = lib.QD_RequestSettings
QD_RequestSettings.restype = c_short
QD_RequestSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestSettings(serial_number)

    return output


QD_RequestStatus = lib.QD_RequestStatus
QD_RequestStatus.restype = c_short
QD_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    '''
    Requests the state quantities (actual power, current and status bits).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestStatus(serial_number)

    return output


QD_RequestStatusBits = lib.QD_RequestStatusBits
QD_RequestStatusBits.restype = c_short
QD_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestStatusBits(serial_number)

    return output


QD_RequestTriggerConfigParams = lib.QD_RequestTriggerConfigParams
QD_RequestTriggerConfigParams.restype = c_short
QD_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    '''
    Requests the trigger config parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_RequestTriggerConfigParams(serial_number)

    return output


QD_SetClosedLoopPosition = lib.QD_SetClosedLoopPosition
QD_SetClosedLoopPosition.restype = c_short
QD_SetClosedLoopPosition.argtypes = [POINTER(c_char)]


def set_closed_loop_position(serial_number):
    '''
    Sets the closed loop position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: QD_ClosedLoopPosition

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = QD_ClosedLoopPosition()

    output = QD_SetClosedLoopPosition(serial_number)

    return output


QD_SetDigitalOutput = lib.QD_SetDigitalOutput
QD_SetDigitalOutput.restype = c_short
QD_SetDigitalOutput.argtypes = [POINTER(c_char)]


def set_digital_output(serial_number):
    '''
    Gets the digital IO parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        digitalIO: QD_KPA_DigitalIO

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    digitalIO = QD_KPA_DigitalIO()

    output = QD_SetDigitalOutput(serial_number)

    return output


QD_SetFrontPanelLock = lib.QD_SetFrontPanelLock
QD_SetFrontPanelLock.restype = c_short
QD_SetFrontPanelLock.argtypes = [POINTER(c_char)]


def set_front_panel_lock(serial_number):
    '''
    Sets the device front panel lock state.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        locked: c_bool

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    locked = c_bool()

    output = QD_SetFrontPanelLock(serial_number)

    return output


QD_SetLEDBrightness = lib.QD_SetLEDBrightness
QD_SetLEDBrightness.restype = c_short
QD_SetLEDBrightness.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    brightness = c_short()

    output = QD_SetLEDBrightness(serial_number)

    return output


QD_SetLoopPIDparams = lib.QD_SetLoopPIDparams
QD_SetLoopPIDparams.restype = c_short
QD_SetLoopPIDparams.argtypes = [POINTER(c_char)]


def set_loop_p_i_dparams(serial_number):
    '''
    Sets the feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        loopParams: QD_LoopParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    loopParams = QD_LoopParameters()

    output = QD_SetLoopPIDparams(serial_number)

    return output


QD_SetLowPassFilterparams = lib.QD_SetLowPassFilterparams
QD_SetLowPassFilterparams.restype = c_short
QD_SetLowPassFilterparams.argtypes = [POINTER(c_char)]


def set_low_pass_filterparams(serial_number):
    '''
    Sets the low pass filter parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        lowPassParams: QD_LowPassFilterParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    lowPassParams = QD_LowPassFilterParameters()

    output = QD_SetLowPassFilterparams(serial_number)

    return output


QD_SetNotchFilterparams = lib.QD_SetNotchFilterparams
QD_SetNotchFilterparams.restype = c_short
QD_SetNotchFilterparams.argtypes = [POINTER(c_char)]


def set_notch_filterparams(serial_number):
    '''
    Sets the notch filter parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalIntegralDerivativeParams: QD_NotchFilterParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalIntegralDerivativeParams = QD_NotchFilterParameters()

    output = QD_SetNotchFilterparams(serial_number)

    return output


QD_SetOperatingMode = lib.QD_SetOperatingMode
QD_SetOperatingMode.restype = c_short
QD_SetOperatingMode.argtypes = [POINTER(c_char)]


def set_operating_mode(serial_number):
    '''
    Sets the operating mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: QD_OperatingMode
        autoOpenCloseLoop: c_bool

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = QD_OperatingMode()
    autoOpenCloseLoop = c_bool()

    output = QD_SetOperatingMode(serial_number)

    return output


QD_SetPIDparams = lib.QD_SetPIDparams
QD_SetPIDparams.restype = c_short
QD_SetPIDparams.argtypes = [POINTER(c_char)]


def set_p_i_dparams(serial_number):
    '''
    Sets the feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalIntegralDerivativeParams: QD_PIDParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalIntegralDerivativeParams = QD_PIDParameters()

    output = QD_SetPIDparams(serial_number)

    return output


QD_SetPosDemandParams = lib.QD_SetPosDemandParams
QD_SetPosDemandParams.restype = c_short
QD_SetPosDemandParams.argtypes = [POINTER(c_char)]


def set_pos_demand_params(serial_number):
    '''
    Sets the position demand parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        demandParams: QD_PositionDemandParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    demandParams = QD_PositionDemandParameters()

    output = QD_SetPosDemandParams(serial_number)

    return output


QD_SetPosition = lib.QD_SetPosition
QD_SetPosition.restype = c_short
QD_SetPosition.argtypes = [POINTER(c_char)]


def set_position(serial_number):
    '''
    Sets position demand output.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: QD_Position

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = QD_Position()

    output = QD_SetPosition(serial_number)

    return output


QD_SetTriggerConfigParams = lib.QD_SetTriggerConfigParams
QD_SetTriggerConfigParams.restype = c_short
QD_SetTriggerConfigParams.argtypes = [POINTER(c_char)]


def set_trigger_config_params(serial_number):
    '''
    Sets the trigger config parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerParams: QD_KPA_TrigIOConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerParams = QD_KPA_TrigIOConfig()

    output = QD_SetTriggerConfigParams(serial_number)

    return output


QD_StartPolling = lib.QD_StartPolling
QD_StartPolling.restype = c_bool
QD_StartPolling.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    milliseconds = c_int()

    output = QD_StartPolling(serial_number)

    return output


QD_StopPolling = lib.QD_StopPolling
QD_StopPolling.restype = c_void_p
QD_StopPolling.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = QD_StopPolling(serial_number)

    return output


QD_TimeSinceLastMsgReceived = lib.QD_TimeSinceLastMsgReceived
QD_TimeSinceLastMsgReceived.restype = c_bool
QD_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    lastUpdateTimeMS = c_int64()

    output = QD_TimeSinceLastMsgReceived(serial_number)

    return output


QD_WaitForMessage = lib.QD_WaitForMessage
QD_WaitForMessage.restype = c_bool
QD_WaitForMessage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = QD_WaitForMessage(serial_number)

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
TLI_GetDeviceInfo.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    serialNumber = POINTER(c_char)()
    info = TLI_DeviceInfo()

    output = TLI_GetDeviceInfo(serial_number)

    return output


TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]


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
TLI_GetDeviceListByType.argtypes = [SafeArray]


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

    return output


TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char)]


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

    return output


TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray]


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

    return output


TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char)]


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

    return output


TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char)]


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

    return output


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

    return output


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



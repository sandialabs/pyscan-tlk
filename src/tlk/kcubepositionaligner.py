from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (QD_OperatingMode)
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
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = QD_CanDeviceLockFrontPanel(serial_number)

    return output


QD_CheckConnection = lib.QD_CheckConnection
QD_CheckConnection.restype = c_bool
QD_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = QD_CheckConnection(serial_number)

    return output


QD_ClearMessageQueue = lib.QD_ClearMessageQueue
QD_ClearMessageQueue.restype = c_void_p
QD_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = QD_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_Close = lib.QD_Close
QD_Close.restype = c_void_p
QD_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = QD_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_EnableLastMsgTimer = lib.QD_EnableLastMsgTimer
QD_EnableLastMsgTimer.restype = c_void_p
QD_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = QD_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


QD_GetClosedLoopPosition = lib.QD_GetClosedLoopPosition
QD_GetClosedLoopPosition.restype = c_short
QD_GetClosedLoopPosition.argtypes = [POINTER(c_char), QD_ClosedLoopPosition]


def get_closed_loop_position(serial_number):
    # Gets closed loop position.

    serial_number = POINTER(c_char)
    position = QD_ClosedLoopPosition()

    output = QD_GetClosedLoopPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


QD_GetDemandedPosition = lib.QD_GetDemandedPosition
QD_GetDemandedPosition.restype = c_short
QD_GetDemandedPosition.argtypes = [POINTER(c_char), QD_Position]


def get_demanded_position(serial_number):
    # Gets position demand output.

    serial_number = POINTER(c_char)
    position = QD_Position()

    output = QD_GetDemandedPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


QD_GetDigitalOutput = lib.QD_GetDigitalOutput
QD_GetDigitalOutput.restype = c_short
QD_GetDigitalOutput.argtypes = [POINTER(c_char), QD_KPA_DigitalIO]


def get_digital_output(serial_number):
    # Sets the digital IO parameters.

    serial_number = POINTER(c_char)
    digitalIO = QD_KPA_DigitalIO()

    output = QD_GetDigitalOutput(serial_number, digitalIO)
    if output != 0:
        raise KinesisException(output)


QD_GetFirmwareVersion = lib.QD_GetFirmwareVersion
QD_GetFirmwareVersion.restype = c_ulong
QD_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = QD_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_GetFrontPanelLocked = lib.QD_GetFrontPanelLocked
QD_GetFrontPanelLocked.restype = c_bool
QD_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = QD_GetFrontPanelLocked(serial_number)

    return output


QD_GetHardwareInfo = lib.QD_GetHardwareInfo
QD_GetHardwareInfo.restype = c_short
QD_GetHardwareInfo.argtypes = [
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

    output = QD_GetHardwareInfo(
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


QD_GetHardwareInfoBlock = lib.QD_GetHardwareInfoBlock
QD_GetHardwareInfoBlock.restype = c_short
QD_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = QD_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


QD_GetLEDBrightness = lib.QD_GetLEDBrightness
QD_GetLEDBrightness.restype = c_long
QD_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_l_e_d_brightness(serial_number):
    # Gets the LED brightness.

    serial_number = POINTER(c_char)

    output = QD_GetLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_GetLoopPIDparams = lib.QD_GetLoopPIDparams
QD_GetLoopPIDparams.restype = c_short
QD_GetLoopPIDparams.argtypes = [POINTER(c_char), QD_LoopParameters]


def get_loop_p_i_dparams(serial_number):
    # Gets the feedback loop parameters.

    serial_number = POINTER(c_char)
    loopParams = QD_LoopParameters()

    output = QD_GetLoopPIDparams(serial_number, loopParams)
    if output != 0:
        raise KinesisException(output)


QD_GetLowPassFilterparams = lib.QD_GetLowPassFilterparams
QD_GetLowPassFilterparams.restype = c_short
QD_GetLowPassFilterparams.argtypes = [POINTER(c_char), QD_LowPassFilterParameters]


def get_low_pass_filterparams(serial_number):
    # Gets the low pass filter parameters.

    serial_number = POINTER(c_char)
    lowPassParams = QD_LowPassFilterParameters()

    output = QD_GetLowPassFilterparams(serial_number, lowPassParams)
    if output != 0:
        raise KinesisException(output)


QD_GetNextMessage = lib.QD_GetNextMessage
QD_GetNextMessage.restype = c_bool
QD_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = QD_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


QD_GetNotchFilterparams = lib.QD_GetNotchFilterparams
QD_GetNotchFilterparams.restype = c_short
QD_GetNotchFilterparams.argtypes = [POINTER(c_char), QD_NotchFilterParameters]


def get_notch_filterparams(serial_number):
    # Gets the notch filter parameters.

    serial_number = POINTER(c_char)
    notchParams = QD_NotchFilterParameters()

    output = QD_GetNotchFilterparams(serial_number, notchParams)
    if output != 0:
        raise KinesisException(output)


QD_GetOperatingMode = lib.QD_GetOperatingMode
QD_GetOperatingMode.restype = QD_OperatingMode
QD_GetOperatingMode.argtypes = [POINTER(c_char)]


def get_operating_mode(serial_number):
    # Gets the operating mode.

    serial_number = POINTER(c_char)

    output = QD_GetOperatingMode(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_GetPIDparams = lib.QD_GetPIDparams
QD_GetPIDparams.restype = c_short
QD_GetPIDparams.argtypes = [POINTER(c_char), QD_PIDParameters]


def get_p_i_dparams(serial_number):
    # Gets the feedback loop parameters.

    serial_number = POINTER(c_char)
    proportionalIntegralDerivativeParams = QD_PIDParameters()

    output = QD_GetPIDparams(serial_number, proportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


QD_GetPosDemandParams = lib.QD_GetPosDemandParams
QD_GetPosDemandParams.restype = c_short
QD_GetPosDemandParams.argtypes = [POINTER(c_char), QD_PositionDemandParameters]


def get_pos_demand_params(serial_number):
    # Gets the position demand output parameters.

    serial_number = POINTER(c_char)
    demandParams = QD_PositionDemandParameters()

    output = QD_GetPosDemandParams(serial_number, demandParams)
    if output != 0:
        raise KinesisException(output)


QD_GetReading = lib.QD_GetReading
QD_GetReading.restype = c_short
QD_GetReading.argtypes = [POINTER(c_char), QD_Readings]


def get_reading(serial_number):
    # Gets a reading.

    serial_number = POINTER(c_char)
    reading = QD_Readings()

    output = QD_GetReading(serial_number, reading)
    if output != 0:
        raise KinesisException(output)


QD_GetSoftwareVersion = lib.QD_GetSoftwareVersion
QD_GetSoftwareVersion.restype = c_ulong
QD_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = QD_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_GetStatusBits = lib.QD_GetStatusBits
QD_GetStatusBits.restype = c_ulong
QD_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = QD_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_GetTriggerConfigParams = lib.QD_GetTriggerConfigParams
QD_GetTriggerConfigParams.restype = c_short
QD_GetTriggerConfigParams.argtypes = [POINTER(c_char), QD_KPA_TrigIOConfig]


def get_trigger_config_params(serial_number):
    # Gets the trigger config parameters.

    serial_number = POINTER(c_char)
    triggerParams = QD_KPA_TrigIOConfig()

    output = QD_GetTriggerConfigParams(serial_number, triggerParams)
    if output != 0:
        raise KinesisException(output)


QD_HasLastMsgTimerOverrun = lib.QD_HasLastMsgTimerOverrun
QD_HasLastMsgTimerOverrun.restype = c_bool
QD_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by QD_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = QD_HasLastMsgTimerOverrun(serial_number)

    return output


QD_Identify = lib.QD_Identify
QD_Identify.restype = c_void_p
QD_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = QD_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_LoadNamedSettings = lib.QD_LoadNamedSettings
QD_LoadNamedSettings.restype = c_bool
QD_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = QD_LoadNamedSettings(serial_number, settingsName)

    return output


QD_LoadSettings = lib.QD_LoadSettings
QD_LoadSettings.restype = c_bool
QD_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = QD_LoadSettings(serial_number)

    return output


QD_MessageQueueSize = lib.QD_MessageQueueSize
QD_MessageQueueSize.restype = c_int
QD_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = QD_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_Open = lib.QD_Open
QD_Open.restype = c_short
QD_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = QD_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_PersistSettings = lib.QD_PersistSettings
QD_PersistSettings.restype = c_bool
QD_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = QD_PersistSettings(serial_number)

    return output


QD_PollingDuration = lib.QD_PollingDuration
QD_PollingDuration.restype = c_long
QD_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = QD_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RegisterMessageCallback = lib.QD_RegisterMessageCallback
QD_RegisterMessageCallback.restype = c_void_p
QD_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = QD_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


QD_RequestClosedLoopPosition = lib.QD_RequestClosedLoopPosition
QD_RequestClosedLoopPosition.restype = c_short
QD_RequestClosedLoopPosition.argtypes = [POINTER(c_char)]


def request_closed_loop_position(serial_number):
    # Request the closed loop position.

    serial_number = POINTER(c_char)

    output = QD_RequestClosedLoopPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestDigitalOutput = lib.QD_RequestDigitalOutput
QD_RequestDigitalOutput.restype = c_short
QD_RequestDigitalOutput.argtypes = [POINTER(c_char)]


def request_digital_output(serial_number):
    # Requests the digital IO parameters.

    serial_number = POINTER(c_char)

    output = QD_RequestDigitalOutput(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestFrontPanelLocked = lib.QD_RequestFrontPanelLocked
QD_RequestFrontPanelLocked.restype = c_short
QD_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = QD_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestLEDBrightness = lib.QD_RequestLEDBrightness
QD_RequestLEDBrightness.restype = c_short
QD_RequestLEDBrightness.argtypes = [POINTER(c_char)]


def request_l_e_d_brightness(serial_number):
    # Requests the LED brightness.

    serial_number = POINTER(c_char)

    output = QD_RequestLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestLoopPIDparams = lib.QD_RequestLoopPIDparams
QD_RequestLoopPIDparams.restype = c_short
QD_RequestLoopPIDparams.argtypes = [POINTER(c_char)]


def request_loop_p_i_dparams(serial_number):
    # Requests the feedback loop parameters.

    serial_number = POINTER(c_char)

    output = QD_RequestLoopPIDparams(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestOperatingMode = lib.QD_RequestOperatingMode
QD_RequestOperatingMode.restype = c_short
QD_RequestOperatingMode.argtypes = [POINTER(c_char)]


def request_operating_mode(serial_number):
    # Requests the operating mode.

    serial_number = POINTER(c_char)

    output = QD_RequestOperatingMode(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestPosDemandParams = lib.QD_RequestPosDemandParams
QD_RequestPosDemandParams.restype = c_short
QD_RequestPosDemandParams.argtypes = [POINTER(c_char)]


def request_pos_demand_params(serial_number):
    # Requests the position demand output parameters.

    serial_number = POINTER(c_char)

    output = QD_RequestPosDemandParams(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestReading = lib.QD_RequestReading
QD_RequestReading.restype = c_short
QD_RequestReading.argtypes = [POINTER(c_char)]


def request_reading(serial_number):
    # Request reading.

    serial_number = POINTER(c_char)

    output = QD_RequestReading(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestSettings = lib.QD_RequestSettings
QD_RequestSettings.restype = c_short
QD_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = QD_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestStatus = lib.QD_RequestStatus
QD_RequestStatus.restype = c_short
QD_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the state quantities (actual power, current and status bits).

    serial_number = POINTER(c_char)

    output = QD_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestStatusBits = lib.QD_RequestStatusBits
QD_RequestStatusBits.restype = c_short
QD_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = QD_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_RequestTriggerConfigParams = lib.QD_RequestTriggerConfigParams
QD_RequestTriggerConfigParams.restype = c_short
QD_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    # Requests the trigger config parameters.

    serial_number = POINTER(c_char)

    output = QD_RequestTriggerConfigParams(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_SetClosedLoopPosition = lib.QD_SetClosedLoopPosition
QD_SetClosedLoopPosition.restype = c_short
QD_SetClosedLoopPosition.argtypes = [POINTER(c_char), QD_ClosedLoopPosition]


def set_closed_loop_position(serial_number):
    # Sets the closed loop position.

    serial_number = POINTER(c_char)
    position = QD_ClosedLoopPosition()

    output = QD_SetClosedLoopPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


QD_SetDigitalOutput = lib.QD_SetDigitalOutput
QD_SetDigitalOutput.restype = c_short
QD_SetDigitalOutput.argtypes = [POINTER(c_char), QD_KPA_DigitalIO]


def set_digital_output(serial_number):
    # Gets the digital IO parameters.

    serial_number = POINTER(c_char)
    digitalIO = QD_KPA_DigitalIO()

    output = QD_SetDigitalOutput(serial_number, digitalIO)
    if output != 0:
        raise KinesisException(output)


QD_SetFrontPanelLock = lib.QD_SetFrontPanelLock
QD_SetFrontPanelLock.restype = c_short
QD_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = QD_SetFrontPanelLock(serial_number, locked)
    if output != 0:
        raise KinesisException(output)


QD_SetLEDBrightness = lib.QD_SetLEDBrightness
QD_SetLEDBrightness.restype = c_short
QD_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_l_e_d_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = POINTER(c_char)
    brightness = c_short()

    output = QD_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


QD_SetLoopPIDparams = lib.QD_SetLoopPIDparams
QD_SetLoopPIDparams.restype = c_short
QD_SetLoopPIDparams.argtypes = [POINTER(c_char), QD_LoopParameters]


def set_loop_p_i_dparams(serial_number):
    # Sets the feedback loop parameters.

    serial_number = POINTER(c_char)
    loopParams = QD_LoopParameters()

    output = QD_SetLoopPIDparams(serial_number, loopParams)
    if output != 0:
        raise KinesisException(output)


QD_SetLowPassFilterparams = lib.QD_SetLowPassFilterparams
QD_SetLowPassFilterparams.restype = c_short
QD_SetLowPassFilterparams.argtypes = [POINTER(c_char), QD_LowPassFilterParameters]


def set_low_pass_filterparams(serial_number):
    # Sets the low pass filter parameters.

    serial_number = POINTER(c_char)
    lowPassParams = QD_LowPassFilterParameters()

    output = QD_SetLowPassFilterparams(serial_number, lowPassParams)
    if output != 0:
        raise KinesisException(output)


QD_SetNotchFilterparams = lib.QD_SetNotchFilterparams
QD_SetNotchFilterparams.restype = c_short
QD_SetNotchFilterparams.argtypes = [POINTER(c_char), QD_NotchFilterParameters]


def set_notch_filterparams(serial_number):
    # Sets the notch filter parameters.

    serial_number = POINTER(c_char)
    proportionalIntegralDerivativeParams = QD_NotchFilterParameters()

    output = QD_SetNotchFilterparams(serial_number, proportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


QD_SetOperatingMode = lib.QD_SetOperatingMode
QD_SetOperatingMode.restype = c_short
QD_SetOperatingMode.argtypes = [POINTER(c_char), QD_OperatingMode, c_bool]


def set_operating_mode(serial_number):
    # Sets the operating mode.

    serial_number = POINTER(c_char)
    mode = QD_OperatingMode()
    autoOpenCloseLoop = c_bool()

    output = QD_SetOperatingMode(serial_number, mode, autoOpenCloseLoop)
    if output != 0:
        raise KinesisException(output)


QD_SetPIDparams = lib.QD_SetPIDparams
QD_SetPIDparams.restype = c_short
QD_SetPIDparams.argtypes = [POINTER(c_char), QD_PIDParameters]


def set_p_i_dparams(serial_number):
    # Sets the feedback loop parameters.

    serial_number = POINTER(c_char)
    proportionalIntegralDerivativeParams = QD_PIDParameters()

    output = QD_SetPIDparams(serial_number, proportionalIntegralDerivativeParams)
    if output != 0:
        raise KinesisException(output)


QD_SetPosDemandParams = lib.QD_SetPosDemandParams
QD_SetPosDemandParams.restype = c_short
QD_SetPosDemandParams.argtypes = [POINTER(c_char), QD_PositionDemandParameters]


def set_pos_demand_params(serial_number):
    # Sets the position demand parameters.

    serial_number = POINTER(c_char)
    demandParams = QD_PositionDemandParameters()

    output = QD_SetPosDemandParams(serial_number, demandParams)
    if output != 0:
        raise KinesisException(output)


QD_SetPosition = lib.QD_SetPosition
QD_SetPosition.restype = c_short
QD_SetPosition.argtypes = [POINTER(c_char), QD_Position]


def set_position(serial_number):
    # Sets position demand output.

    serial_number = POINTER(c_char)
    position = QD_Position()

    output = QD_SetPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


QD_SetTriggerConfigParams = lib.QD_SetTriggerConfigParams
QD_SetTriggerConfigParams.restype = c_short
QD_SetTriggerConfigParams.argtypes = [POINTER(c_char), QD_KPA_TrigIOConfig]


def set_trigger_config_params(serial_number):
    # Sets the trigger config parameters.

    serial_number = POINTER(c_char)
    triggerParams = QD_KPA_TrigIOConfig()

    output = QD_SetTriggerConfigParams(serial_number, triggerParams)
    if output != 0:
        raise KinesisException(output)


QD_StartPolling = lib.QD_StartPolling
QD_StartPolling.restype = c_bool
QD_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = QD_StartPolling(serial_number, milliseconds)

    return output


QD_StopPolling = lib.QD_StopPolling
QD_StopPolling.restype = c_void_p
QD_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = QD_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


QD_TimeSinceLastMsgReceived = lib.QD_TimeSinceLastMsgReceived
QD_TimeSinceLastMsgReceived.restype = c_bool
QD_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = QD_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


QD_WaitForMessage = lib.QD_WaitForMessage
QD_WaitForMessage.restype = c_bool
QD_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = QD_WaitForMessage(serial_number, messageType, messageID, messageData)

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

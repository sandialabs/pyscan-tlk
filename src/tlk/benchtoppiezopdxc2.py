from ctypes import (POINTER, c_bool, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    MOT_TravelDirection,
    PDXC2_TriggerModes,
    PZ_AmpOutParameters,
    PZ_ControlModeTypes,
    PZ_StageAxisParameters)
from .definitions.structures import (
    PDXC2_ClosedLoopParameters,
    PDXC2_JogParameters,
    PDXC2_OpenLoopMoveParameters,
    PDXC2_TriggerParams,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "MotionControl.Benchtop.Piezo.DLL")

PDXC2_CheckConnection = lib.PDXC2_CheckConnection
PDXC2_CheckConnection.restype = c_bool
PDXC2_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = PDXC2_CheckConnection(serial_number)

    return output


PDXC2_ClearMessageQueue = lib.PDXC2_ClearMessageQueue
PDXC2_ClearMessageQueue.restype = c_short
PDXC2_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = PDXC2_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_Close = lib.PDXC2_Close
PDXC2_Close.restype = c_void_p
PDXC2_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = PDXC2_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_Disable = lib.PDXC2_Disable
PDXC2_Disable.restype = c_short
PDXC2_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)

    output = PDXC2_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_Disconnect = lib.PDXC2_Disconnect
PDXC2_Disconnect.restype = c_short
PDXC2_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = PDXC2_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_Enable = lib.PDXC2_Enable
PDXC2_Enable.restype = c_short
PDXC2_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)

    output = PDXC2_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_EnableLastMsgTimer = lib.PDXC2_EnableLastMsgTimer
PDXC2_EnableLastMsgTimer.restype = c_void_p
PDXC2_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = PDXC2_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetAbnormalMoveDetectionEnabled = lib.PDXC2_GetAbnormalMoveDetectionEnabled
PDXC2_GetAbnormalMoveDetectionEnabled.restype = c_bool
PDXC2_GetAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char)]


def get_abnormal_move_detection_enabled(serial_number):
    # Gets the abnormal mode detection state.

    serial_number = POINTER(c_char)

    output = PDXC2_GetAbnormalMoveDetectionEnabled(serial_number)

    return output


PDXC2_GetAmpOutParams = lib.PDXC2_GetAmpOutParams
PDXC2_GetAmpOutParams.restype = c_short
PDXC2_GetAmpOutParams.argtypes = [POINTER(c_char), PZ_AmpOutParameters]


def get_amp_out_params(serial_number):
    # Gets the amplifier output parameters.

    serial_number = POINTER(c_char)
    params = PZ_AmpOutParameters()

    output = PDXC2_GetAmpOutParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetClosedLoopParams = lib.PDXC2_GetClosedLoopParams
PDXC2_GetClosedLoopParams.restype = c_short
PDXC2_GetClosedLoopParams.argtypes = [POINTER(c_char), PDXC2_ClosedLoopParameters]


def get_closed_loop_params(serial_number):
    # Gets the closed loop parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_ClosedLoopParameters()

    output = PDXC2_GetClosedLoopParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetClosedLoopTarget = lib.PDXC2_GetClosedLoopTarget
PDXC2_GetClosedLoopTarget.restype = c_int
PDXC2_GetClosedLoopTarget.argtypes = [POINTER(c_char)]


def get_closed_loop_target(serial_number):
    # Gets the closed loop target position.

    serial_number = POINTER(c_char)

    output = PDXC2_GetClosedLoopTarget(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetExternalTriggerConfig = lib.PDXC2_GetExternalTriggerConfig
PDXC2_GetExternalTriggerConfig.restype = PDXC2_TriggerModes
PDXC2_GetExternalTriggerConfig.argtypes = [POINTER(c_char)]


def get_external_trigger_config(serial_number):
    # Gets the external trigger mode.

    serial_number = POINTER(c_char)

    output = PDXC2_GetExternalTriggerConfig(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetExternalTriggerParams = lib.PDXC2_GetExternalTriggerParams
PDXC2_GetExternalTriggerParams.restype = c_short
PDXC2_GetExternalTriggerParams.argtypes = [POINTER(c_char), PDXC2_TriggerParams]


def get_external_trigger_params(serial_number):
    # Gets the external trigger parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_TriggerParams()

    output = PDXC2_GetExternalTriggerParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetExternalTriggerTarget = lib.PDXC2_GetExternalTriggerTarget
PDXC2_GetExternalTriggerTarget.restype = c_int
PDXC2_GetExternalTriggerTarget.argtypes = [POINTER(c_char)]


def get_external_trigger_target(serial_number):
    # Gets the external trigger target.

    serial_number = POINTER(c_char)

    output = PDXC2_GetExternalTriggerTarget(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetFirmwareVersion = lib.PDXC2_GetFirmwareVersion
PDXC2_GetFirmwareVersion.restype = c_ulong
PDXC2_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = PDXC2_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetHardwareInfo = lib.PDXC2_GetHardwareInfo
PDXC2_GetHardwareInfo.restype = c_short
PDXC2_GetHardwareInfo.argtypes = [
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

    output = PDXC2_GetHardwareInfo(
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


PDXC2_GetHardwareInfoBlock = lib.PDXC2_GetHardwareInfoBlock
PDXC2_GetHardwareInfoBlock.restype = c_short
PDXC2_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = PDXC2_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetJogParams = lib.PDXC2_GetJogParams
PDXC2_GetJogParams.restype = c_short
PDXC2_GetJogParams.argtypes = [POINTER(c_char), PDXC2_JogParameters]


def get_jog_params(serial_number):
    # Gets the jog parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_JogParameters()

    output = PDXC2_GetJogParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetNextMessage = lib.PDXC2_GetNextMessage
PDXC2_GetNextMessage.restype = c_bool
PDXC2_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PDXC2_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


PDXC2_GetOpenLoopMoveParams = lib.PDXC2_GetOpenLoopMoveParams
PDXC2_GetOpenLoopMoveParams.restype = c_short
PDXC2_GetOpenLoopMoveParams.argtypes = [POINTER(c_char), PDXC2_OpenLoopMoveParameters]


def get_open_loop_move_params(serial_number):
    # Gets the open loop move parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_OpenLoopMoveParameters()

    output = PDXC2_GetOpenLoopMoveParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetPosition = lib.PDXC2_GetPosition
PDXC2_GetPosition.restype = c_short
PDXC2_GetPosition.argtypes = [POINTER(c_char), c_int32]


def get_position(serial_number):
    # Get the current position.

    serial_number = POINTER(c_char)
    position = c_int32()

    output = PDXC2_GetPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetPositionControlMode = lib.PDXC2_GetPositionControlMode
PDXC2_GetPositionControlMode.restype = PZ_ControlModeTypes
PDXC2_GetPositionControlMode.argtypes = [POINTER(c_char)]


def get_position_control_mode(serial_number):
    # Gets the Position Control Mode.

    serial_number = POINTER(c_char)

    output = PDXC2_GetPositionControlMode(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetSoftwareVersion = lib.PDXC2_GetSoftwareVersion
PDXC2_GetSoftwareVersion.restype = c_ulong
PDXC2_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = PDXC2_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetStageAxisParams = lib.PDXC2_GetStageAxisParams
PDXC2_GetStageAxisParams.restype = c_short
PDXC2_GetStageAxisParams.argtypes = [POINTER(c_char), PZ_StageAxisParameters]


def get_stage_axis_params(serial_number):
    # Gets the stage axis parameters.

    serial_number = POINTER(c_char)
    params = PZ_StageAxisParameters()

    output = PDXC2_GetStageAxisParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_GetStatusBits = lib.PDXC2_GetStatusBits
PDXC2_GetStatusBits.restype = c_ulong
PDXC2_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = PDXC2_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_HasLastMsgTimerOverrun = lib.PDXC2_HasLastMsgTimerOverrun
PDXC2_HasLastMsgTimerOverrun.restype = c_bool
PDXC2_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by PDXC2_EnableLastMsgTimer(char const * serialNo,
    # bool enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = PDXC2_HasLastMsgTimerOverrun(serial_number)

    return output


PDXC2_Home = lib.PDXC2_Home
PDXC2_Home.restype = c_short
PDXC2_Home.argtypes = [POINTER(c_char)]


def home(serial_number):
    # Sets the current position to the Home position (Position = 0).

    serial_number = POINTER(c_char)

    output = PDXC2_Home(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_Identify = lib.PDXC2_Identify
PDXC2_Identify.restype = c_void_p
PDXC2_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = PDXC2_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_LoadNamedSettings = lib.PDXC2_LoadNamedSettings
PDXC2_LoadNamedSettings.restype = c_bool
PDXC2_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = PDXC2_LoadNamedSettings(serial_number, settingsName)

    return output


PDXC2_LoadSettings = lib.PDXC2_LoadSettings
PDXC2_LoadSettings.restype = c_bool
PDXC2_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = PDXC2_LoadSettings(serial_number)

    return output


PDXC2_MessageQueueSize = lib.PDXC2_MessageQueueSize
PDXC2_MessageQueueSize.restype = c_int
PDXC2_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = PDXC2_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_MoveJog = lib.PDXC2_MoveJog
PDXC2_MoveJog.restype = c_short
PDXC2_MoveJog.argtypes = [POINTER(c_char), MOT_TravelDirection]


def move_jog(serial_number):
    # Move jog.

    serial_number = POINTER(c_char)
    jogDirection = MOT_TravelDirection()

    output = PDXC2_MoveJog(serial_number, jogDirection)
    if output != 0:
        raise KinesisException(output)


PDXC2_MoveStart = lib.PDXC2_MoveStart
PDXC2_MoveStart.restype = c_short
PDXC2_MoveStart.argtypes = [POINTER(c_char)]


def move_start(serial_number):
    # Move start.

    serial_number = POINTER(c_char)

    output = PDXC2_MoveStart(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_MoveStop = lib.PDXC2_MoveStop
PDXC2_MoveStop.restype = c_short
PDXC2_MoveStop.argtypes = [POINTER(c_char)]


def move_stop(serial_number):
    # Move stop.

    serial_number = POINTER(c_char)

    output = PDXC2_MoveStop(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_Open = lib.PDXC2_Open
PDXC2_Open.restype = c_short
PDXC2_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = PDXC2_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_PersistSettings = lib.PDXC2_PersistSettings
PDXC2_PersistSettings.restype = c_bool
PDXC2_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # Persist device settings to device.

    serial_number = POINTER(c_char)

    output = PDXC2_PersistSettings(serial_number)

    return output


PDXC2_PollingDuration = lib.PDXC2_PollingDuration
PDXC2_PollingDuration.restype = c_long
PDXC2_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = PDXC2_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_PulseParamsAcquireStart = lib.PDXC2_PulseParamsAcquireStart
PDXC2_PulseParamsAcquireStart.restype = c_short
PDXC2_PulseParamsAcquireStart.argtypes = [POINTER(c_char)]


def pulse_params_acquire_start(serial_number):
    # Start pulse parameter acquistion.

    serial_number = POINTER(c_char)

    output = PDXC2_PulseParamsAcquireStart(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RegisterMessageCallback = lib.PDXC2_RegisterMessageCallback
PDXC2_RegisterMessageCallback.restype = c_short
PDXC2_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = PDXC2_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestAbnormalMoveDetectionEnabled = lib.PDXC2_RequestAbnormalMoveDetectionEnabled
PDXC2_RequestAbnormalMoveDetectionEnabled.restype = c_short
PDXC2_RequestAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char)]


def request_abnormal_move_detection_enabled(serial_number):
    # Request the abnormal mode detection state.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestAbnormalMoveDetectionEnabled(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestAmpOutParams = lib.PDXC2_RequestAmpOutParams
PDXC2_RequestAmpOutParams.restype = c_short
PDXC2_RequestAmpOutParams.argtypes = [POINTER(c_char)]


def request_amp_out_params(serial_number):
    # Request the amplifier output parameters.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestAmpOutParams(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestClosedLoopParams = lib.PDXC2_RequestClosedLoopParams
PDXC2_RequestClosedLoopParams.restype = c_short
PDXC2_RequestClosedLoopParams.argtypes = [POINTER(c_char)]


def request_closed_loop_params(serial_number):
    # Request the closed loop parameters.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestClosedLoopParams(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestClosedLoopTarget = lib.PDXC2_RequestClosedLoopTarget
PDXC2_RequestClosedLoopTarget.restype = c_short
PDXC2_RequestClosedLoopTarget.argtypes = [POINTER(c_char)]


def request_closed_loop_target(serial_number):
    # Request the closed loop target position.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestClosedLoopTarget(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestExternalTriggerConfig = lib.PDXC2_RequestExternalTriggerConfig
PDXC2_RequestExternalTriggerConfig.restype = c_short
PDXC2_RequestExternalTriggerConfig.argtypes = [POINTER(c_char)]


def request_external_trigger_config(serial_number):
    # Request the external trigger mode.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestExternalTriggerConfig(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestExternalTriggerParams = lib.PDXC2_RequestExternalTriggerParams
PDXC2_RequestExternalTriggerParams.restype = c_short
PDXC2_RequestExternalTriggerParams.argtypes = [POINTER(c_char)]


def request_external_trigger_params(serial_number):
    # Request the external trigger parameters.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestExternalTriggerParams(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestExternalTriggerTarget = lib.PDXC2_RequestExternalTriggerTarget
PDXC2_RequestExternalTriggerTarget.restype = c_short
PDXC2_RequestExternalTriggerTarget.argtypes = [POINTER(c_char)]


def request_external_trigger_target(serial_number):
    # Request the external trigger target.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestExternalTriggerTarget(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestJogParams = lib.PDXC2_RequestJogParams
PDXC2_RequestJogParams.restype = c_short
PDXC2_RequestJogParams.argtypes = [POINTER(c_char)]


def request_jog_params(serial_number):
    # Request the jog parameters.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestJogParams(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestOpenLoopMoveParams = lib.PDXC2_RequestOpenLoopMoveParams
PDXC2_RequestOpenLoopMoveParams.restype = c_short
PDXC2_RequestOpenLoopMoveParams.argtypes = [POINTER(c_char)]


def request_open_loop_move_params(serial_number):
    # Request the open loop move parameters.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestOpenLoopMoveParams(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestPosition = lib.PDXC2_RequestPosition
PDXC2_RequestPosition.restype = c_short
PDXC2_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Requests the current position.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestPositionControlMode = lib.PDXC2_RequestPositionControlMode
PDXC2_RequestPositionControlMode.restype = c_bool
PDXC2_RequestPositionControlMode.argtypes = [POINTER(c_char)]


def request_position_control_mode(serial_number):
    # Sets the Position Control Mode.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestPositionControlMode(serial_number)

    return output


PDXC2_RequestSettings = lib.PDXC2_RequestSettings
PDXC2_RequestSettings.restype = c_short
PDXC2_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestStageAxisParams = lib.PDXC2_RequestStageAxisParams
PDXC2_RequestStageAxisParams.restype = c_short
PDXC2_RequestStageAxisParams.argtypes = [POINTER(c_char)]


def request_stage_axis_params(serial_number):
    # Requests the stage axis parameters.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestStageAxisParams(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestStatus = lib.PDXC2_RequestStatus
PDXC2_RequestStatus.restype = c_short
PDXC2_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the status bits and position.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_RequestStatusBits = lib.PDXC2_RequestStatusBits
PDXC2_RequestStatusBits.restype = c_short
PDXC2_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = PDXC2_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_ResetParameters = lib.PDXC2_ResetParameters
PDXC2_ResetParameters.restype = c_short
PDXC2_ResetParameters.argtypes = [POINTER(c_char)]


def reset_parameters(serial_number):
    # Resets all parameters to power-up values.

    serial_number = POINTER(c_char)

    output = PDXC2_ResetParameters(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetAbnormalMoveDetectionEnabled = lib.PDXC2_SetAbnormalMoveDetectionEnabled
PDXC2_SetAbnormalMoveDetectionEnabled.restype = c_short
PDXC2_SetAbnormalMoveDetectionEnabled.argtypes = [POINTER(c_char), c_bool]


def set_abnormal_move_detection_enabled(serial_number):
    # Sets the abnormal mode detection state.

    serial_number = POINTER(c_char)
    isEnabled = c_bool()

    output = PDXC2_SetAbnormalMoveDetectionEnabled(serial_number, isEnabled)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetAmpOutParams = lib.PDXC2_SetAmpOutParams
PDXC2_SetAmpOutParams.restype = c_short
PDXC2_SetAmpOutParams.argtypes = [POINTER(c_char), PZ_AmpOutParameters]


def set_amp_out_params(serial_number):
    # Sets the amplifier output parameters.

    serial_number = POINTER(c_char)
    params = PZ_AmpOutParameters()

    output = PDXC2_SetAmpOutParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetClosedLoopParams = lib.PDXC2_SetClosedLoopParams
PDXC2_SetClosedLoopParams.restype = c_short
PDXC2_SetClosedLoopParams.argtypes = [POINTER(c_char), PDXC2_ClosedLoopParameters]


def set_closed_loop_params(serial_number):
    # Sets the closed loop parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_ClosedLoopParameters()

    output = PDXC2_SetClosedLoopParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetClosedLoopTarget = lib.PDXC2_SetClosedLoopTarget
PDXC2_SetClosedLoopTarget.restype = c_short
PDXC2_SetClosedLoopTarget.argtypes = [POINTER(c_char), c_int]


def set_closed_loop_target(serial_number):
    # Sets the closed loop target position.

    serial_number = POINTER(c_char)
    target = c_int()

    output = PDXC2_SetClosedLoopTarget(serial_number, target)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetExternalTriggerConfig = lib.PDXC2_SetExternalTriggerConfig
PDXC2_SetExternalTriggerConfig.restype = c_short
PDXC2_SetExternalTriggerConfig.argtypes = [POINTER(c_char), PDXC2_TriggerModes]


def set_external_trigger_config(serial_number):
    # Sets the external trigger mode.

    serial_number = POINTER(c_char)
    mode = PDXC2_TriggerModes()

    output = PDXC2_SetExternalTriggerConfig(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetExternalTriggerParams = lib.PDXC2_SetExternalTriggerParams
PDXC2_SetExternalTriggerParams.restype = c_short
PDXC2_SetExternalTriggerParams.argtypes = [POINTER(c_char), PDXC2_TriggerParams]


def set_external_trigger_params(serial_number):
    # Sets the external trigger parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_TriggerParams()

    output = PDXC2_SetExternalTriggerParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetJogParams = lib.PDXC2_SetJogParams
PDXC2_SetJogParams.restype = c_short
PDXC2_SetJogParams.argtypes = [POINTER(c_char), PDXC2_JogParameters]


def set_jog_params(serial_number):
    # Sets the jog parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_JogParameters()

    output = PDXC2_SetJogParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetOpenLoopMoveParams = lib.PDXC2_SetOpenLoopMoveParams
PDXC2_SetOpenLoopMoveParams.restype = c_short
PDXC2_SetOpenLoopMoveParams.argtypes = [POINTER(c_char), PDXC2_OpenLoopMoveParameters]


def set_open_loop_move_params(serial_number):
    # Sets the open loop move parameters.

    serial_number = POINTER(c_char)
    params = PDXC2_OpenLoopMoveParameters()

    output = PDXC2_SetOpenLoopMoveParams(serial_number, params)
    if output != 0:
        raise KinesisException(output)


PDXC2_SetPositionControlMode = lib.PDXC2_SetPositionControlMode
PDXC2_SetPositionControlMode.restype = c_short
PDXC2_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]


def set_position_control_mode(serial_number):
    # Sets the Position Control Mode.

    serial_number = POINTER(c_char)
    mode = PZ_ControlModeTypes()

    output = PDXC2_SetPositionControlMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


PDXC2_StartPolling = lib.PDXC2_StartPolling
PDXC2_StartPolling.restype = c_bool
PDXC2_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = PDXC2_StartPolling(serial_number, milliseconds)

    return output


PDXC2_StopPolling = lib.PDXC2_StopPolling
PDXC2_StopPolling.restype = c_void_p
PDXC2_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = PDXC2_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


PDXC2_TimeSinceLastMsgReceived = lib.PDXC2_TimeSinceLastMsgReceived
PDXC2_TimeSinceLastMsgReceived.restype = c_bool
PDXC2_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = PDXC2_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


PDXC2_WaitForMessage = lib.PDXC2_WaitForMessage
PDXC2_WaitForMessage.restype = c_bool
PDXC2_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PDXC2_WaitForMessage(serial_number, messageType, messageID, messageData)

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


TLI_ScanEthernetRange = lib.TLI_ScanEthernetRange
TLI_ScanEthernetRange.restype = c_short
TLI_ScanEthernetRange.argtypes = [POINTER(c_char), POINTER(c_char), c_int, c_int, POINTER(c_char), c_ulong]


def scan_ethernet_range():
    # Scans a range of addresses and returns a list of the ip addresses of Thorlabs devices found.

    output = TLI_ScanEthernetRange()
    if output != 0:
        raise KinesisException(output)

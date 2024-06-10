from ctypes import (POINTER, c_bool, c_char, c_int, c_int16, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KIM_Channels,
    KIM_DirectionSense,
    KIM_FBSignalMode,
    KIM_JogMode,
    KIM_JoysticModes,
    KIM_LimitSwitchModes,
    KIM_Stages,
    KIM_TravelDirection,
    KIM_TrigModes,
     KIM_TrigPolarities)
from .definitions.structures import (
    KIM_DriveOPParameters,
    KIM_FeedbackSigParams,
    KIM_HomeParameters,
    KIM_JogParameters,
    KIM_LimitSwitchParameters,
    KIM_MMIChannelParameters,
    KIM_MMIParameters,
    KIM_TrigIOConfig,
    KIM_TrigParamsParameters,
    TLI_DeviceInfo,
     TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.DCServo.dll")

KIM_CanDeviceLockFrontPanel = lib.KIM_CanDeviceLockFrontPanel
KIM_CanDeviceLockFrontPanel.restype = c_bool
KIM_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_pane):
    # Determine if the device front panel can be locked.

    serialNumber=POINTER(c_char)

    output=KIM_CanDeviceLockFrontPanel(serialNumber)

    return output
KIM_CheckConnection=lib.KIM_CheckConnection
KIM_CheckConnection.restype=c_bool
KIM_CheckConnection.argtypes=[POINTER(c_char)]
def check_connectio):
    # Check connection.

    serialNumber=POINTER(c_char)

    output=KIM_CheckConnection(serialNumber)

    return output
KIM_ClearMessageQueue=lib.KIM_ClearMessageQueue
KIM_ClearMessageQueue.restype=c_void_p
KIM_ClearMessageQueue.argtypes=[POINTER(c_char)]
def clear_message_queu):
    # Clears the device message queue.

    serialNumber=POINTER(c_char)

    output=KIM_ClearMessageQueue(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_Close=lib.KIM_Close
KIM_Close.restype=c_void_p
KIM_Close.argtypes=[POINTER(c_char)]
def close_devic):
    # Disconnect and close the device.

    serialNumber=POINTER(c_char)

    output=KIM_Close(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_Disable=lib.KIM_Disable
KIM_Disable.restype=c_short
KIM_Disable.argtypes=[POINTER(c_char)]
def disabl):
    # Disable cube.

    serialNumber=POINTER(c_char)

    output=KIM_Disable(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_DisableChannel=lib.KIM_DisableChannel
KIM_DisableChannel.restype=c_short
KIM_DisableChannel.argtypes=[POINTER(c_char), KIM_Channels]
def disable_channel(channel):
    # Disable a channel.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_DisableChannel(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_Disconnect=lib.KIM_Disconnect
KIM_Disconnect.restype=c_short
KIM_Disconnect.argtypes=[POINTER(c_char)]
def disconnec):
    # Tells the device that it is being disconnected.

    serialNumber=POINTER(c_char)

    output=KIM_Disconnect(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_Enable=lib.KIM_Enable
KIM_Enable.restype=c_short
KIM_Enable.argtypes=[POINTER(c_char)]
def enabl):
    # Enable cube for computer control.

    serialNumber=POINTER(c_char)

    output=KIM_Enable(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_EnableChannel=lib.KIM_EnableChannel
KIM_EnableChannel.restype=c_short
KIM_EnableChannel.argtypes=[POINTER(c_char), KIM_Channels]
def enable_channel(channel):
    # Enable a channel.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_EnableChannel(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_EnableLastMsgTimer=lib.KIM_EnableLastMsgTimer
KIM_EnableLastMsgTimer.restype=c_void_p
KIM_EnableLastMsgTimer.argtypes=[POINTER(c_char), c_bool, c_int32]
def enable_last_msg_time):
    # Enables the last message monitoring timer.

    serialNumber=POINTER(c_char)
    enable=c_bool()
    lastMsgTimeout=c_int32()

    output=KIM_EnableLastMsgTimer(serialNumber, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)
KIM_GetAbsoluteMoveParameters=lib.KIM_GetAbsoluteMoveParameters
KIM_GetAbsoluteMoveParameters.restype=c_short
KIM_GetAbsoluteMoveParameters.argtypes=[POINTER(c_char), KIM_Channels, c_int32]
def get_absolute_move_parameters(channel):
    # Gets a absolute move parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    absoluteMove=c_int32()

    output=KIM_GetAbsoluteMoveParameters(serialNumber, channel, absoluteMove)
    if output != 0:
        raise KinesisException(output)
KIM_GetCurrentPosition=lib.KIM_GetCurrentPosition
KIM_GetCurrentPosition.restype=c_int32
KIM_GetCurrentPosition.argtypes=[POINTER(c_char), KIM_Channels]
def get_current_position(channel):
    # Gets current position.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_GetCurrentPosition(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_GetDriveOPParameters=lib.KIM_GetDriveOPParameters
KIM_GetDriveOPParameters.restype=c_short
KIM_GetDriveOPParameters.argtypes=[POINTER(c_char), KIM_Channels, c_int16, c_int32, c_int32]
def get_drive_o_p_parameters(channel):
    # Gets the operation drive parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    maxVoltage=c_int16()
    stepRate=c_int32()
    stepAcceleration=c_int32()

    output=KIM_GetDriveOPParameters(serialNumber, channel, maxVoltage, stepRate, stepAcceleration)
    if output != 0:
        raise KinesisException(output)
KIM_GetDriveOPParametersStruct=lib.KIM_GetDriveOPParametersStruct
KIM_GetDriveOPParametersStruct.restype=c_short
KIM_GetDriveOPParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_DriveOPParameters]
def get_drive_o_p_parameters_struct(channel):
    # Gets the operation drive parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    driveOPParameters=KIM_DriveOPParameters()

    output=KIM_GetDriveOPParametersStruct(serialNumber, channel, driveOPParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetFeedbackSigParameters=lib.KIM_GetFeedbackSigParameters
KIM_GetFeedbackSigParameters.restype=c_short
KIM_GetFeedbackSigParameters.argtypes=[POINTER(c_char), KIM_Channels, KIM_FBSignalMode, c_int32]
def get_feedback_sig_parameters(channel):
    # Gets a feedback signal parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    feedbackSignalMode=KIM_FBSignalMode()
    encoderConst=c_int32()

    output=KIM_GetFeedbackSigParameters(serialNumber, channel, feedbackSignalMode, encoderConst)
    if output != 0:
        raise KinesisException(output)
KIM_GetFeedbackSigParametersStruct=lib.KIM_GetFeedbackSigParametersStruct
KIM_GetFeedbackSigParametersStruct.restype=c_short
KIM_GetFeedbackSigParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_FeedbackSigParams]
def get_feedback_sig_parameters_struct(channel):
    # Gets a feedback signal parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    fbSigParameters=KIM_FeedbackSigParams()

    output=KIM_GetFeedbackSigParametersStruct(serialNumber, channel, fbSigParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetFirmwareVersion=lib.KIM_GetFirmwareVersion
KIM_GetFirmwareVersion.restype=c_ulong
KIM_GetFirmwareVersion.argtypes=[POINTER(c_char)]
def get_firmware_versio):
    # Gets version number of the device firmware.

    serialNumber=POINTER(c_char)

    output=KIM_GetFirmwareVersion(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_GetFrontPanelLocked=lib.KIM_GetFrontPanelLocked
KIM_GetFrontPanelLocked.restype=c_bool
KIM_GetFrontPanelLocked.argtypes=[POINTER(c_char)]
def get_front_panel_locke):
    # Query if the device front panel locked.

    serialNumber=POINTER(c_char)

    output=KIM_GetFrontPanelLocked(serialNumber)

    return output
KIM_GetHardwareInfo=lib.KIM_GetHardwareInfo
KIM_GetHardwareInfo.restype=c_short
KIM_GetHardwareInfo.argtypes=[
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
def get_hardware_inf):
    # Gets the hardware information from the device.

    serialNumber=POINTER(c_char)
    modelNo=POINTER(c_char)
    sizeOfModelNo=c_ulong()
    type=c_long()
    numChannels=c_long()
    notes=POINTER(c_char)
    sizeOfNotes=c_ulong()
    firmwareVersion=c_ulong()
    hardwareVersion=c_long()
    modificationState=c_long()

    output=KIM_GetHardwareInfo(
    serialNumber,
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
KIM_GetHardwareInfoBlock=lib.KIM_GetHardwareInfoBlock
KIM_GetHardwareInfoBlock.restype=c_short
KIM_GetHardwareInfoBlock.argtypes=[POINTER(c_char), TLI_HardwareInformation]
def get_hardware_info_bloc):
    # Gets the hardware information in a block.

    serialNumber=POINTER(c_char)
    hardwareInfo=TLI_HardwareInformation()

    output=KIM_GetHardwareInfoBlock(serialNumber, hardwareInfo)
    if output != 0:
        raise KinesisException(output)
KIM_GetHomeParameters=lib.KIM_GetHomeParameters
KIM_GetHomeParameters.restype=c_short
KIM_GetHomeParameters.argtypes=[
    POINTER(c_char),
    KIM_Channels,
    KIM_TravelDirection,
    KIM_TravelDirection,
    c_int32,
     c_int32]
def get_home_parameters(channel):
    # Gets a home parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    homeDirection=KIM_TravelDirection()
    homeLimitSwitch=KIM_TravelDirection()
    homeStepRate=c_int32()
    homeOffset=c_int32()

    output=KIM_GetHomeParameters(serialNumber, channel, homeDirection, homeLimitSwitch, homeStepRate, homeOffset)
    if output != 0:
        raise KinesisException(output)
KIM_GetHomeParametersStruct=lib.KIM_GetHomeParametersStruct
KIM_GetHomeParametersStruct.restype=c_short
KIM_GetHomeParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_HomeParameters]
def get_home_parameters_struct(channel):
    # Gets a home parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    homeParameters=KIM_HomeParameters()

    output=KIM_GetHomeParametersStruct(serialNumber, channel, homeParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetJogParameters=lib.KIM_GetJogParameters
KIM_GetJogParameters.restype=c_short
KIM_GetJogParameters.argtypes=[POINTER(c_char), KIM_Channels, KIM_JogMode, c_int32, c_int32, c_int32, c_int32]
def get_jog_parameters(channel):
    # Gets the jog parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    jogMode=KIM_JogMode()
    jogStepSizeFwd=c_int32()
    jogStepSizeRev=c_int32()
    jogStepRate=c_int32()
    jogStepAcceleration=c_int32()

    output=KIM_GetJogParameters(
    serialNumber,
    channel,
    jogMode,
    jogStepSizeFwd,
    jogStepSizeRev,
    jogStepRate,
     jogStepAcceleration)
    if output != 0:
        raise KinesisException(output)
KIM_GetJogParametersStruct=lib.KIM_GetJogParametersStruct
KIM_GetJogParametersStruct.restype=c_short
KIM_GetJogParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_JogParameters]
def get_jog_parameters_struct(channel):
    # Gets the jog parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    jogParameters=KIM_JogParameters()

    output=KIM_GetJogParametersStruct(serialNumber, channel, jogParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetLimitSwitchParameters=lib.KIM_GetLimitSwitchParameters
KIM_GetLimitSwitchParameters.restype=c_short
KIM_GetLimitSwitchParameters.argtypes=[
    POINTER(c_char),
    KIM_Channels,
    KIM_LimitSwitchModes,
    KIM_LimitSwitchModes,
     c_int16]
def get_limit_switch_parameters(channel):
    # Gets a limit switch parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    forwardLimit=KIM_LimitSwitchModes()
    reverseLimit=KIM_LimitSwitchModes()
    stageID=c_int16()

    output=KIM_GetLimitSwitchParameters(serialNumber, channel, forwardLimit, reverseLimit, stageID)
    if output != 0:
        raise KinesisException(output)
KIM_GetLimitSwitchParametersStruct=lib.KIM_GetLimitSwitchParametersStruct
KIM_GetLimitSwitchParametersStruct.restype=c_short
KIM_GetLimitSwitchParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_LimitSwitchParameters]
def get_limit_switch_parameters_struct(channel):
    # Gets a limit switch parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    limitSwitchParameters=KIM_LimitSwitchParameters()

    output=KIM_GetLimitSwitchParametersStruct(serialNumber, channel, limitSwitchParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetMMIChannelParameters=lib.KIM_GetMMIChannelParameters
KIM_GetMMIChannelParameters.restype=c_short
KIM_GetMMIChannelParameters.argtypes=[POINTER(c_char), KIM_Channels, c_int32, c_int32]
def get_m_m_i_channel_parameters(channel):
    # Gets a mmi parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    presetPos1=c_int32()
    presetPos2=c_int32()

    output=KIM_GetMMIChannelParameters(serialNumber, channel, presetPos1, presetPos2)
    if output != 0:
        raise KinesisException(output)
KIM_GetMMIChannelParametersStruct=lib.KIM_GetMMIChannelParametersStruct
KIM_GetMMIChannelParametersStruct.restype=c_short
KIM_GetMMIChannelParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_MMIChannelParameters]
def get_m_m_i_channel_parameters_struct(channel):
    # Gets a mmi parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    mmiParameters=KIM_MMIChannelParameters()

    output=KIM_GetMMIChannelParametersStruct(serialNumber, channel, mmiParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetMMIDeviceParameters=lib.KIM_GetMMIDeviceParameters
KIM_GetMMIDeviceParameters.restype=c_short
KIM_GetMMIDeviceParameters.argtypes=[
    POINTER(c_char),
    KIM_Channels,
    KIM_JoysticModes,
    c_int32,
    KIM_DirectionSense,
    c_int32,
    c_int32,
     c_int32]
def get_m_m_i_device_parameters(channel):
    # Gets a mmi parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    joystickMode=KIM_JoysticModes()
    maxStepRate=c_int32()
    directionSense=KIM_DirectionSense()
    presetPos1=c_int32()
    presetPos2=c_int32()
    displayIntensity=c_int32()

    output=KIM_GetMMIDeviceParameters(
    serialNumber,
    channel,
    joystickMode,
    maxStepRate,
    directionSense,
    presetPos1,
    presetPos2,
     displayIntensity)
    if output != 0:
        raise KinesisException(output)
KIM_GetMMIDeviceParametersStruct=lib.KIM_GetMMIDeviceParametersStruct
KIM_GetMMIDeviceParametersStruct.restype=c_short
KIM_GetMMIDeviceParametersStruct.argtypes=[POINTER(c_char), KIM_MMIParameters]
def get_m_m_i_device_parameters_struc):
    # Gets a mmi parameters.

    serialNumber=POINTER(c_char)
    mmiParameters=KIM_MMIParameters()

    output=KIM_GetMMIDeviceParametersStruct(serialNumber, mmiParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetNextMessage=lib.KIM_GetNextMessage
KIM_GetNextMessage.restype=c_bool
KIM_GetNextMessage.argtypes=[POINTER(c_char), c_long, c_long, c_ulong]
def get_next_messag):
    # Get the next MessageQueue item.

    serialNumber=POINTER(c_char)
    messageType=c_long()
    messageID=c_long()
    messageData=c_ulong()

    output=KIM_GetNextMessage(serialNumber, messageType, messageID, messageData)

    return output
KIM_GetRelativeMoveParameter=lib.KIM_GetRelativeMoveParameter
KIM_GetRelativeMoveParameter.restype=c_short
KIM_GetRelativeMoveParameter.argtypes=[POINTER(c_char), KIM_Channels, c_int32]
def get_relative_move_parameter(channel):
    # Gets a relative move parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    relativeMoveStep=c_int32()

    output=KIM_GetRelativeMoveParameter(serialNumber, channel, relativeMoveStep)
    if output != 0:
        raise KinesisException(output)
KIM_GetSoftwareVersion=lib.KIM_GetSoftwareVersion
KIM_GetSoftwareVersion.restype=c_ulong
KIM_GetSoftwareVersion.argtypes=[POINTER(c_char)]
def get_software_versio):
    # Gets version number of the device software.

    serialNumber=POINTER(c_char)

    output=KIM_GetSoftwareVersion(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_GetStageType=lib.KIM_GetStageType
KIM_GetStageType.restype=KIM_Stages
KIM_GetStageType.argtypes=[POINTER(c_char)]
def get_stage_typ):
    # Gets the KIM stage type.

    serialNumber=POINTER(c_char)

    output=KIM_GetStageType(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_GetStatusBits=lib.KIM_GetStatusBits
KIM_GetStatusBits.restype=c_ulong
KIM_GetStatusBits.argtypes=[POINTER(c_char), KIM_Channels]
def get_status_bits(channel):
    # Tc get status bits.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_GetStatusBits(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_GetTrigIOParameters=lib.KIM_GetTrigIOParameters
KIM_GetTrigIOParameters.restype=c_short
KIM_GetTrigIOParameters.argtypes=[
    POINTER(c_char),
    KIM_TrigModes,
    KIM_TrigPolarities,
    KIM_Channels,
    KIM_TrigModes,
    KIM_TrigPolarities,
     KIM_Channels]
def get_trig_i_o_parameter):
    # Gets a trig IO parameters.

    serialNumber=POINTER(c_char)
    trig1Mode=KIM_TrigModes()
    trig1Polarity=KIM_TrigPolarities()
    trigChannel1=KIM_Channels()
    trig2Mode=KIM_TrigModes()
    trig2Polarity=KIM_TrigPolarities()
    trigChannel2=KIM_Channels()

    output=KIM_GetTrigIOParameters(
    serialNumber,
    trig1Mode,
    trig1Polarity,
    trigChannel1,
    trig2Mode,
    trig2Polarity,
     trigChannel2)
    if output != 0:
        raise KinesisException(output)
KIM_GetTrigIOParametersStruct=lib.KIM_GetTrigIOParametersStruct
KIM_GetTrigIOParametersStruct.restype=c_short
KIM_GetTrigIOParametersStruct.argtypes=[POINTER(c_char), KIM_TrigIOConfig]
def get_trig_i_o_parameters_struc):
    # Gets a trig IO parameters.

    serialNumber=POINTER(c_char)
    trigIOParameters=KIM_TrigIOConfig()

    output=KIM_GetTrigIOParametersStruct(serialNumber, trigIOParameters)
    if output != 0:
        raise KinesisException(output)
KIM_GetTrigParamsParameters=lib.KIM_GetTrigParamsParameters
KIM_GetTrigParamsParameters.restype=c_short
KIM_GetTrigParamsParameters.argtypes=[
    POINTER(c_char),
    KIM_Channels,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
     c_int32]
def get_trig_params_parameters(channel):
    # Gets a trigger parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    startPosFwd=c_int32()
    intervalFwd=c_int32()
    numberOfPulsesFwd=c_int32()
    startPosRev=c_int32()
    intervalRev=c_int32()
    numberOfPulsesRev=c_int32()
    pulseWidth=c_int32()
    numberOfCycles=c_int32()

    output=KIM_GetTrigParamsParameters(
    serialNumber,
    channel,
    startPosFwd,
    intervalFwd,
    numberOfPulsesFwd,
    startPosRev,
    intervalRev,
    numberOfPulsesRev,
    pulseWidth,
     numberOfCycles)
    if output != 0:
        raise KinesisException(output)
KIM_GetTrigParamsParametersStruct=lib.KIM_GetTrigParamsParametersStruct
KIM_GetTrigParamsParametersStruct.restype=c_short
KIM_GetTrigParamsParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_TrigParamsParameters]
def get_trig_params_parameters_struct(channel):
    # Gets a trigger parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    trigParameters=KIM_TrigParamsParameters()

    output=KIM_GetTrigParamsParametersStruct(serialNumber, channel, trigParameters)
    if output != 0:
        raise KinesisException(output)
KIM_HasLastMsgTimerOverrun=lib.KIM_HasLastMsgTimerOverrun
KIM_HasLastMsgTimerOverrun.restype=c_bool
KIM_HasLastMsgTimerOverrun.argtypes=[POINTER(c_char)]
def has_last_msg_timer_overru):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by KIM_EnableLastMsgTimer(char const * serialNumber,
    # bool enable, __int32 lastMsgTimeout ).

    serialNumber=POINTER(c_char)

    output=KIM_HasLastMsgTimerOverrun(serialNumber)

    return output
KIM_Home=lib.KIM_Home
KIM_Home.restype=c_short
KIM_Home.argtypes=[POINTER(c_char), KIM_Channels]
def home(channel):
    # Home the device to a limit switch or reset to zero if no limit switches available.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_Home(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_Identify=lib.KIM_Identify
KIM_Identify.restype=c_void_p
KIM_Identify.argtypes=[POINTER(c_char)]
def identif):
    # Sends a command to the device to make it identify iteself.

    serialNumber=POINTER(c_char)

    output=KIM_Identify(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_IsDualChannelMode=lib.KIM_IsDualChannelMode
KIM_IsDualChannelMode.restype=c_bool
KIM_IsDualChannelMode.argtypes=[POINTER(c_char)]
def is_dual_channel_mod):
    # Gets the Dual Channel Mode state.

    serialNumber=POINTER(c_char)

    output=KIM_IsDualChannelMode(serialNumber)

    return output
KIM_LoadNamedSettings=lib.KIM_LoadNamedSettings
KIM_LoadNamedSettings.restype=c_bool
KIM_LoadNamedSettings.argtypes=[POINTER(c_char), POINTER(c_char)]
def load_named_setting):
    # Update device with named settings.

    serialNumber=POINTER(c_char)
    settingsName=POINTER(c_char)

    output=KIM_LoadNamedSettings(serialNumber, settingsName)

    return output
KIM_LoadSettings=lib.KIM_LoadSettings
KIM_LoadSettings.restype=c_bool
KIM_LoadSettings.argtypes=[POINTER(c_char)]
def load_setting):
    # Update device with stored settings.

    serialNumber=POINTER(c_char)

    output=KIM_LoadSettings(serialNumber)

    return output
KIM_MessageQueueSize=lib.KIM_MessageQueueSize
KIM_MessageQueueSize.restype=c_int
KIM_MessageQueueSize.argtypes=[POINTER(c_char)]
def message_queue_siz):
    # Gets the MessageQueue size.

    serialNumber=POINTER(c_char)

    output=KIM_MessageQueueSize(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_MoveAbsolute=lib.KIM_MoveAbsolute
KIM_MoveAbsolute.restype=c_short
KIM_MoveAbsolute.argtypes=[POINTER(c_char), KIM_Channels, c_int32]
def move_absolute(channel):
    # Move absolute.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    position=c_int32()

    output=KIM_MoveAbsolute(serialNumber, channel, position)
    if output != 0:
        raise KinesisException(output)
KIM_MoveJog=lib.KIM_MoveJog
KIM_MoveJog.restype=c_short
KIM_MoveJog.argtypes=[POINTER(c_char), KIM_Channels, KIM_TravelDirection]
def move_jog(channel):
    # Move jog.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    jogDirection=KIM_TravelDirection()

    output=KIM_MoveJog(serialNumber, channel, jogDirection)
    if output != 0:
        raise KinesisException(output)
KIM_MoveRelative=lib.KIM_MoveRelative
KIM_MoveRelative.restype=c_short
KIM_MoveRelative.argtypes=[POINTER(c_char), KIM_Channels, c_int32]
def move_relative(channel):
    # Move relative.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    stepSize=c_int32()

    output=KIM_MoveRelative(serialNumber, channel, stepSize)
    if output != 0:
        raise KinesisException(output)
KIM_MoveStop=lib.KIM_MoveStop
KIM_MoveStop.restype=c_short
KIM_MoveStop.argtypes=[POINTER(c_char), KIM_Channels]
def move_stop(channel):
    # Move stop.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_MoveStop(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_Open=lib.KIM_Open
KIM_Open.restype=c_short
KIM_Open.argtypes=[POINTER(c_char)]
def open_devic):
    # Open the device for communications.

    serialNumber=POINTER(c_char)

    output=KIM_Open(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_PersistSettings=lib.KIM_PersistSettings
KIM_PersistSettings.restype=c_bool
KIM_PersistSettings.argtypes=[POINTER(c_char)]
def persist_setting):
    # persist the devices current settings.

    serialNumber=POINTER(c_char)

    output=KIM_PersistSettings(serialNumber)

    return output
KIM_PollingDuration=lib.KIM_PollingDuration
KIM_PollingDuration.restype=c_long
KIM_PollingDuration.argtypes=[POINTER(c_char)]
def polling_duratio):
    # Gets the polling loop duration.

    serialNumber=POINTER(c_char)

    output=KIM_PollingDuration(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_RegisterMessageCallback=lib.KIM_RegisterMessageCallback
KIM_RegisterMessageCallback.restype=c_void_p
KIM_RegisterMessageCallback.argtypes=[POINTER(c_char), c_void_p]
def register_message_callbac):
    # Registers a callback on the message queue.

    serialNumber=POINTER(c_char)
    void=c_void_p()

    output=KIM_RegisterMessageCallback(serialNumber, void)
    if output != 0:
        raise KinesisException(output)
KIM_RequestAbsoluteMoveParameters=lib.KIM_RequestAbsoluteMoveParameters
KIM_RequestAbsoluteMoveParameters.restype=c_short
KIM_RequestAbsoluteMoveParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_absolute_move_parameters(channel):
    # Request the absolute move parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestAbsoluteMoveParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestCurrentPosition=lib.KIM_RequestCurrentPosition
KIM_RequestCurrentPosition.restype=c_short
KIM_RequestCurrentPosition.argtypes=[POINTER(c_char), KIM_Channels]
def request_current_position(channel):
    # Requests the current position.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestCurrentPosition(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestDriveOPParameters=lib.KIM_RequestDriveOPParameters
KIM_RequestDriveOPParameters.restype=c_short
KIM_RequestDriveOPParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_drive_o_p_parameters(channel):
    # Requests the operation drive parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestDriveOPParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestFeedbackSigParameters=lib.KIM_RequestFeedbackSigParameters
KIM_RequestFeedbackSigParameters.restype=c_short
KIM_RequestFeedbackSigParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_feedback_sig_parameters(channel):
    # Request the feedback signal parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestFeedbackSigParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestFrontPanelLocked=lib.KIM_RequestFrontPanelLocked
KIM_RequestFrontPanelLocked.restype=c_short
KIM_RequestFrontPanelLocked.argtypes=[POINTER(c_char)]
def request_front_panel_locke):
    # Ask the device if its front panel is locked.

    serialNumber=POINTER(c_char)

    output=KIM_RequestFrontPanelLocked(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_RequestHomeParameters=lib.KIM_RequestHomeParameters
KIM_RequestHomeParameters.restype=c_short
KIM_RequestHomeParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_home_parameters(channel):
    # Request the home parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestHomeParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestJogParameters=lib.KIM_RequestJogParameters
KIM_RequestJogParameters.restype=c_short
KIM_RequestJogParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_jog_parameters(channel):
    # Requests the jog parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestJogParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestLimitSwitchParameters=lib.KIM_RequestLimitSwitchParameters
KIM_RequestLimitSwitchParameters.restype=c_short
KIM_RequestLimitSwitchParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_limit_switch_parameters(channel):
    # Request the limit switch parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestLimitSwitchParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestMMIParameters=lib.KIM_RequestMMIParameters
KIM_RequestMMIParameters.restype=c_short
KIM_RequestMMIParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_m_m_i_parameters(channel):
    # Request the mmi parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestMMIParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestRelativeMoveParameter=lib.KIM_RequestRelativeMoveParameter
KIM_RequestRelativeMoveParameter.restype=c_short
KIM_RequestRelativeMoveParameter.argtypes=[POINTER(c_char), KIM_Channels]
def request_relative_move_parameter(channel):
    # Request the relative move parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestRelativeMoveParameter(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_RequestSettings=lib.KIM_RequestSettings
KIM_RequestSettings.restype=c_short
KIM_RequestSettings.argtypes=[POINTER(c_char)]
def request_setting):
    # Requests that all settings are download from device.

    serialNumber=POINTER(c_char)

    output=KIM_RequestSettings(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_RequestStageType=lib.KIM_RequestStageType
KIM_RequestStageType.restype=c_short
KIM_RequestStageType.argtypes=[POINTER(c_char)]
def request_stage_typ):
    # Request KIM stage type.

    serialNumber=POINTER(c_char)

    output=KIM_RequestStageType(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_RequestStatus=lib.KIM_RequestStatus
KIM_RequestStatus.restype=c_short
KIM_RequestStatus.argtypes=[POINTER(c_char)]
def request_statu):
    # Requests the state quantities (actual temperature, current and status bits).

    serialNumber=POINTER(c_char)

    output=KIM_RequestStatus(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_RequestStatusBits=lib.KIM_RequestStatusBits
KIM_RequestStatusBits.restype=c_short
KIM_RequestStatusBits.argtypes=[POINTER(c_char)]
def request_status_bit):
    # Request the status bits which identify the current device state.

    serialNumber=POINTER(c_char)

    output=KIM_RequestStatusBits(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_RequestTrigIOParameters=lib.KIM_RequestTrigIOParameters
KIM_RequestTrigIOParameters.restype=c_short
KIM_RequestTrigIOParameters.argtypes=[POINTER(c_char)]
def request_trig_i_o_parameter):
    # Request the trig IO parameters.

    serialNumber=POINTER(c_char)

    output=KIM_RequestTrigIOParameters(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_RequestTrigParamsParameters=lib.KIM_RequestTrigParamsParameters
KIM_RequestTrigParamsParameters.restype=c_short
KIM_RequestTrigParamsParameters.argtypes=[POINTER(c_char), KIM_Channels]
def request_trig_params_parameters(channel):
    # Request the trigger parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_RequestTrigParamsParameters(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
KIM_Reset=lib.KIM_Reset
KIM_Reset.restype=c_short
KIM_Reset.argtypes=[POINTER(c_char)]
def rese):
    # Reset the device.

    serialNumber=POINTER(c_char)

    output=KIM_Reset(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_SetAbsoluteMoveParameters=lib.KIM_SetAbsoluteMoveParameters
KIM_SetAbsoluteMoveParameters.restype=c_short
KIM_SetAbsoluteMoveParameters.argtypes=[POINTER(c_char), KIM_Channels, c_int32]
def set_absolute_move_parameters(channel):
    # Sets the absolute move parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    absoluteMove=c_int32()

    output=KIM_SetAbsoluteMoveParameters(serialNumber, channel, absoluteMove)
    if output != 0:
        raise KinesisException(output)
KIM_SetDriveOPParameters=lib.KIM_SetDriveOPParameters
KIM_SetDriveOPParameters.restype=c_short
KIM_SetDriveOPParameters.argtypes=[POINTER(c_char), KIM_Channels, c_int16, c_int32, c_int32]
def set_drive_o_p_parameters(channel):
    # Sets the operation drive parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    maxVoltage=c_int16()
    stepRate=c_int32()
    stepAcceleration=c_int32()

    output=KIM_SetDriveOPParameters(serialNumber, channel, maxVoltage, stepRate, stepAcceleration)
    if output != 0:
        raise KinesisException(output)
KIM_SetDriveOPParametersStruct=lib.KIM_SetDriveOPParametersStruct
KIM_SetDriveOPParametersStruct.restype=c_short
KIM_SetDriveOPParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_DriveOPParameters]
def set_drive_o_p_parameters_struct(channel):
    # Sets the operation drive parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    driveOPParameters=KIM_DriveOPParameters()

    output=KIM_SetDriveOPParametersStruct(serialNumber, channel, driveOPParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetDualChannelMode=lib.KIM_SetDualChannelMode
KIM_SetDualChannelMode.restype=c_short
KIM_SetDualChannelMode.argtypes=[POINTER(c_char), c_bool]
def set_dual_channel_mod):
    # Sets the Dual Channel Mode.

    serialNumber=POINTER(c_char)
    enableDualChannel=c_bool()

    output=KIM_SetDualChannelMode(serialNumber, enableDualChannel)
    if output != 0:
        raise KinesisException(output)
KIM_SetFeedbackSigParameters=lib.KIM_SetFeedbackSigParameters
KIM_SetFeedbackSigParameters.restype=c_short
KIM_SetFeedbackSigParameters.argtypes=[POINTER(c_char), KIM_Channels, KIM_FBSignalMode, c_int32]
def set_feedback_sig_parameters(channel):
    # Sets the feedback signal parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    feedbackSignalMode=KIM_FBSignalMode()
    encoderConst=c_int32()

    output=KIM_SetFeedbackSigParameters(serialNumber, channel, feedbackSignalMode, encoderConst)
    if output != 0:
        raise KinesisException(output)
KIM_SetFeedbackSigParametersStruct=lib.KIM_SetFeedbackSigParametersStruct
KIM_SetFeedbackSigParametersStruct.restype=c_short
KIM_SetFeedbackSigParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_FeedbackSigParams]
def set_feedback_sig_parameters_struct(channel):
    # Sets the feedback signal parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    fbSigParameters=KIM_FeedbackSigParams()

    output=KIM_SetFeedbackSigParametersStruct(serialNumber, channel, fbSigParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetFrontPanelLock=lib.KIM_SetFrontPanelLock
KIM_SetFrontPanelLock.restype=c_short
KIM_SetFrontPanelLock.argtypes=[POINTER(c_char), c_bool]
def set_front_panel_loc):
    # Sets the device front panel lock state.

    serialNumber=POINTER(c_char)
    locked=c_bool()

    output=KIM_SetFrontPanelLock(serialNumber, locked)
    if output != 0:
        raise KinesisException(output)
KIM_SetHomeParameters=lib.KIM_SetHomeParameters
KIM_SetHomeParameters.restype=c_short
KIM_SetHomeParameters.argtypes=[
    POINTER(c_char),
    KIM_Channels,
    KIM_TravelDirection,
    KIM_TravelDirection,
    c_int32,
     c_int32]
def set_home_parameters(channel):
    # Sets the home parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    homeDirection=KIM_TravelDirection()
    homeLimitSwitch=KIM_TravelDirection()
    homeStepRate=c_int32()
    homeOffset=c_int32()

    output=KIM_SetHomeParameters(serialNumber, channel, homeDirection, homeLimitSwitch, homeStepRate, homeOffset)
    if output != 0:
        raise KinesisException(output)
KIM_SetHomeParametersStruct=lib.KIM_SetHomeParametersStruct
KIM_SetHomeParametersStruct.restype=c_short
KIM_SetHomeParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_HomeParameters]
def set_home_parameters_struct(channel):
    # Sets the home parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    homeParameters=KIM_HomeParameters()

    output=KIM_SetHomeParametersStruct(serialNumber, channel, homeParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetJogParameters=lib.KIM_SetJogParameters
KIM_SetJogParameters.restype=c_short
KIM_SetJogParameters.argtypes=[POINTER(c_char), KIM_Channels, KIM_JogMode, c_int32, c_int32, c_int32, c_int32]
def set_jog_parameters(channel):
    # Sets the jog parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    jogMode=KIM_JogMode()
    jogStepSizeFwd=c_int32()
    jogStepSizeRev=c_int32()
    jogStepRate=c_int32()
    jogStepAcceleration=c_int32()

    output=KIM_SetJogParameters(
    serialNumber,
    channel,
    jogMode,
    jogStepSizeFwd,
    jogStepSizeRev,
    jogStepRate,
     jogStepAcceleration)
    if output != 0:
        raise KinesisException(output)
KIM_SetJogParametersStruct=lib.KIM_SetJogParametersStruct
KIM_SetJogParametersStruct.restype=c_short
KIM_SetJogParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_JogParameters]
def set_jog_parameters_struct(channel):
    # Sets the jog parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    jogParameters=KIM_JogParameters()

    output=KIM_SetJogParametersStruct(serialNumber, channel, jogParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetLimitSwitchParameters=lib.KIM_SetLimitSwitchParameters
KIM_SetLimitSwitchParameters.restype=c_short
KIM_SetLimitSwitchParameters.argtypes=[
    POINTER(c_char),
    KIM_Channels,
    KIM_LimitSwitchModes,
    KIM_LimitSwitchModes,
     c_int16]
def set_limit_switch_parameters(channel):
    # Sets the limit switch parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    forwardLimit=KIM_LimitSwitchModes()
    reverseLimit=KIM_LimitSwitchModes()
    stageID=c_int16()

    output=KIM_SetLimitSwitchParameters(serialNumber, channel, forwardLimit, reverseLimit, stageID)
    if output != 0:
        raise KinesisException(output)
KIM_SetLimitSwitchParametersStruct=lib.KIM_SetLimitSwitchParametersStruct
KIM_SetLimitSwitchParametersStruct.restype=c_short
KIM_SetLimitSwitchParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_LimitSwitchParameters]
def set_limit_switch_parameters_struct(channel):
    # Sets the limit switch parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    limitSwitchParameters=KIM_LimitSwitchParameters()

    output=KIM_SetLimitSwitchParametersStruct(serialNumber, channel, limitSwitchParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetMMIChannelParameters=lib.KIM_SetMMIChannelParameters
KIM_SetMMIChannelParameters.restype=c_short
KIM_SetMMIChannelParameters.argtypes=[POINTER(c_char), KIM_Channels, c_int32, c_int32]
def set_m_m_i_channel_parameters(channel):
    # Sets the mmi parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    presetPos1=c_int32()
    presetPos2=c_int32()

    output=KIM_SetMMIChannelParameters(serialNumber, channel, presetPos1, presetPos2)
    if output != 0:
        raise KinesisException(output)
KIM_SetMMIChannelParametersStruct=lib.KIM_SetMMIChannelParametersStruct
KIM_SetMMIChannelParametersStruct.restype=c_short
KIM_SetMMIChannelParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_MMIChannelParameters]
def set_m_m_i_channel_parameters_struct(channel):
    # Sets the mmi parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    mmiParameters=KIM_MMIChannelParameters()

    output=KIM_SetMMIChannelParametersStruct(serialNumber, channel, mmiParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetMMIDeviceParameters=lib.KIM_SetMMIDeviceParameters
KIM_SetMMIDeviceParameters.restype=c_short
KIM_SetMMIDeviceParameters.argtypes=[POINTER(c_char), KIM_JoysticModes, c_int32, KIM_DirectionSense, c_int16]
def set_m_m_i_device_parameter):
    # Sets the mmi parameters.

    serialNumber=POINTER(c_char)
    joystickMode=KIM_JoysticModes()
    maxStepRate=c_int32()
    directionSense=KIM_DirectionSense()
    displayIntensity=c_int16()

    output=KIM_SetMMIDeviceParameters(serialNumber, joystickMode, maxStepRate, directionSense, displayIntensity)
    if output != 0:
        raise KinesisException(output)
KIM_SetMMIDeviceParametersStruct=lib.KIM_SetMMIDeviceParametersStruct
KIM_SetMMIDeviceParametersStruct.restype=c_short
KIM_SetMMIDeviceParametersStruct.argtypes=[POINTER(c_char), KIM_MMIParameters]
def set_m_m_i_device_parameters_struc):
    # Sets the mmi parameters.

    serialNumber=POINTER(c_char)
    mmiParameters=KIM_MMIParameters()

    output=KIM_SetMMIDeviceParametersStruct(serialNumber, mmiParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetPosition=lib.KIM_SetPosition
KIM_SetPosition.restype=c_short
KIM_SetPosition.argtypes=[POINTER(c_char), KIM_Channels, c_long]
def set_position(channel):
    # set the position.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    position=c_long()

    output=KIM_SetPosition(serialNumber, channel, position)
    if output != 0:
        raise KinesisException(output)
KIM_SetRelativeMoveParameter=lib.KIM_SetRelativeMoveParameter
KIM_SetRelativeMoveParameter.restype=c_short
KIM_SetRelativeMoveParameter.argtypes=[POINTER(c_char), KIM_Channels, c_int32]
def set_relative_move_parameter(channel):
    # Sets the relative move parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    relativeMove=c_int32()

    output=KIM_SetRelativeMoveParameter(serialNumber, channel, relativeMove)
    if output != 0:
        raise KinesisException(output)
KIM_SetStageType=lib.KIM_SetStageType
KIM_SetStageType.restype=c_short
KIM_SetStageType.argtypes=[POINTER(c_char), KIM_Stages]
def set_stage_typ):
    # Sets the KIM stage type.

    serialNumber=POINTER(c_char)
    stageType=KIM_Stages()

    output=KIM_SetStageType(serialNumber, stageType)
    if output != 0:
        raise KinesisException(output)
KIM_SetTrigIOParameters=lib.KIM_SetTrigIOParameters
KIM_SetTrigIOParameters.restype=c_short
KIM_SetTrigIOParameters.argtypes=[
    POINTER(c_char),
    KIM_TrigModes,
    KIM_TrigPolarities,
    KIM_Channels,
    KIM_TrigModes,
    KIM_TrigPolarities,
     KIM_Channels]
def set_trig_i_o_parameter):
    # Sets the limit switch parameters.

    serialNumber=POINTER(c_char)
    trig1Mode=KIM_TrigModes()
    trig1Polarity=KIM_TrigPolarities()
    trigChannel1=KIM_Channels()
    trig2Mode=KIM_TrigModes()
    trig2Polarity=KIM_TrigPolarities()
    trigChannel2=KIM_Channels()

    output=KIM_SetTrigIOParameters(
    serialNumber,
    trig1Mode,
    trig1Polarity,
    trigChannel1,
    trig2Mode,
    trig2Polarity,
     trigChannel2)
    if output != 0:
        raise KinesisException(output)
KIM_SetTrigIOParametersStruct=lib.KIM_SetTrigIOParametersStruct
KIM_SetTrigIOParametersStruct.restype=c_short
KIM_SetTrigIOParametersStruct.argtypes=[POINTER(c_char), KIM_TrigIOConfig]
def set_trig_i_o_parameters_struc):
    # Sets the limit switch parameters.

    serialNumber=POINTER(c_char)
    trigIOParameters=KIM_TrigIOConfig()

    output=KIM_SetTrigIOParametersStruct(serialNumber, trigIOParameters)
    if output != 0:
        raise KinesisException(output)
KIM_SetTrigParamsParameters=lib.KIM_SetTrigParamsParameters
KIM_SetTrigParamsParameters.restype=c_short
KIM_SetTrigParamsParameters.argtypes=[
    POINTER(c_char),
    KIM_Channels,
    KIM_TrigParamsParameters,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
    c_int32,
     c_int32]
def set_trig_params_parameters(channel):
    # Sets the trigger parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    trigParameters=KIM_TrigParamsParameters()
    startPosFwd=c_int32()
    intervalFwd=c_int32()
    numberOfPulsesFwd=c_int32()
    startPosRev=c_int32()
    intervalRev=c_int32()
    numberOfPulsesRev=c_int32()
    pulseWidth=c_int32()
    numberOfCycles=c_int32()

    output=KIM_SetTrigParamsParameters(
    serialNumber,
    channel,
    trigParameters,
    startPosFwd,
    intervalFwd,
    numberOfPulsesFwd,
    startPosRev,
    intervalRev,
    numberOfPulsesRev,
    pulseWidth,
     numberOfCycles)
    if output != 0:
        raise KinesisException(output)
KIM_SetTrigParamsParametersStruct=lib.KIM_SetTrigParamsParametersStruct
KIM_SetTrigParamsParametersStruct.restype=c_short
KIM_SetTrigParamsParametersStruct.argtypes=[POINTER(c_char), KIM_Channels, KIM_TrigParamsParameters]
def set_trig_params_parameters_struct(channel):
    # Sets the trigger parameters.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()
    trigParameters=KIM_TrigParamsParameters()

    output=KIM_SetTrigParamsParametersStruct(serialNumber, channel, trigParameters)
    if output != 0:
        raise KinesisException(output)
KIM_StartPolling=lib.KIM_StartPolling
KIM_StartPolling.restype=c_bool
KIM_StartPolling.argtypes=[POINTER(c_char), c_int]
def start_pollin):
    # Starts the internal polling loop which continuously requests position and status.

    serialNumber=POINTER(c_char)
    milliseconds=c_int()

    output=KIM_StartPolling(serialNumber, milliseconds)

    return output
KIM_StopPolling=lib.KIM_StopPolling
KIM_StopPolling.restype=c_void_p
KIM_StopPolling.argtypes=[POINTER(c_char)]
def stop_pollin):
    # Stops the internal polling loop.

    serialNumber=POINTER(c_char)

    output=KIM_StopPolling(serialNumber)
    if output != 0:
        raise KinesisException(output)
KIM_SupportsDualChannelMode=lib.KIM_SupportsDualChannelMode
KIM_SupportsDualChannelMode.restype=c_bool
KIM_SupportsDualChannelMode.argtypes=[POINTER(c_char)]
def supports_dual_channel_mod):
    # Determines whether the device supports Dual Channel Mode.

    serialNumber=POINTER(c_char)

    output=KIM_SupportsDualChannelMode(serialNumber)

    return output
KIM_SupportsStageType=lib.KIM_SupportsStageType
KIM_SupportsStageType.restype=c_bool
KIM_SupportsStageType.argtypes=[POINTER(c_char)]
def supports_stage_typ):
    # Gets a flag to show whether the KIM stage type is supported.

    serialNumber=POINTER(c_char)

    output=KIM_SupportsStageType(serialNumber)

    return output
KIM_TimeSinceLastMsgReceived=lib.KIM_TimeSinceLastMsgReceived
KIM_TimeSinceLastMsgReceived.restype=c_bool
KIM_TimeSinceLastMsgReceived.argtypes=[POINTER(c_char), c_int64]
def time_since_last_msg_receive):
    # Gets the time in milliseconds since tha last message was received from the device.

    serialNumber=POINTER(c_char)
    lastUpdateTimeMS=c_int64()

    output=KIM_TimeSinceLastMsgReceived(serialNumber, lastUpdateTimeMS)

    return output
KIM_WaitForMessage=lib.KIM_WaitForMessage
KIM_WaitForMessage.restype=c_bool
KIM_WaitForMessage.argtypes=[POINTER(c_char), c_long, c_long, c_ulong]
def wait_for_messag):
    # Wait for next MessageQueue item.

    serialNumber=POINTER(c_char)
    messageType=c_long()
    messageID=c_long()
    messageData=c_ulong()

    output=KIM_WaitForMessage(serialNumber, messageType, messageID, messageData)

    return output
KIM_ZeroPosition=lib.KIM_ZeroPosition
KIM_ZeroPosition.restype=c_short
KIM_ZeroPosition.argtypes=[POINTER(c_char), KIM_Channels]
def zero_position(channel):
    # Sets the current position to zero.

    serialNumber=POINTER(c_char)
    channel=KIM_Channels()

    output=KIM_ZeroPosition(serialNumber, channel)
    if output != 0:
        raise KinesisException(output)
TLI_BuildDeviceList=lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype=c_short
TLI_BuildDeviceList.argtypes=[c_void_p]
def build_device_list():
    # Build the DeviceList.

    output=TLI_BuildDeviceList()
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceInfo=lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype=c_short
TLI_GetDeviceInfo.argtypes=[POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]
def get_device_info(serial_number):
    # Get the device information from the USB port.

    serial_number=POINTER(c_char)
    serialNumber=POINTER(c_char)
    info=TLI_DeviceInfo()

    output=TLI_GetDeviceInfo(serial_number, serialNumber, info)
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceList=lib.TLI_GetDeviceList
TLI_GetDeviceList.restype=c_short
TLI_GetDeviceList.argtypes=[SafeArray]
def get_device_list():
    # Get the entire contents of the device list.

    output=TLI_GetDeviceList()
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceListByType=lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype=c_short
TLI_GetDeviceListByType.argtypes=[SafeArray, c_int]
def get_device_list_by_type():
    # Get the contents of the device list which match the supplied typeID.

    output=TLI_GetDeviceListByType()
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceListByTypeExt=lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype=c_short
TLI_GetDeviceListByTypeExt.argtypes=[POINTER(c_char), c_ulong, c_int]
def get_device_list_by_type_ext():
    # Get the contents of the device list which match the supplied typeID.

    output=TLI_GetDeviceListByTypeExt()
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceListByTypes=lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype=c_short
TLI_GetDeviceListByTypes.argtypes=[SafeArray, c_int, c_int]
def get_device_list_by_types():
    # Get the contents of the device list which match the supplied typeIDs.

    output=TLI_GetDeviceListByTypes()
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceListByTypesExt=lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype=c_short
TLI_GetDeviceListByTypesExt.argtypes=[POINTER(c_char), c_ulong, c_int, c_int]
def get_device_list_by_types_ext():
    # Get the contents of the device list which match the supplied typeIDs.

    output=TLI_GetDeviceListByTypesExt()
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceListExt=lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype=c_short
TLI_GetDeviceListExt.argtypes=[POINTER(c_char), c_ulong]
def get_device_list_ext():
    # Get the entire contents of the device list.

    output=TLI_GetDeviceListExt()
    if output != 0:
        raise KinesisException(output)
TLI_GetDeviceListSize=lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype=c_short
def get_device_list_size():
    # Gets the device list size.

    output=TLI_GetDeviceListSize()
    if output != 0:
        raise KinesisException(output)
TLI_InitializeSimulations=lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype=c_void_p
def initialize_simulations():
    # Initialize a connection to the Simulation Manager, which must already be running.

    output=TLI_InitializeSimulations()
    if output != 0:
        raise KinesisException(output)

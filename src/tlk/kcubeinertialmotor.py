from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_char_p,
    c_int,
    c_int16,
    c_int32,
    c_int64,
    c_long,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
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

c_short_pointer = type(pointer(c_short()))
c_ulong_pointer = type(pointer(c_ulong()))
c_long_pointer = type(pointer(c_ulong()))


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.DCServo.dll")

KIM_CanDeviceLockFrontPanel = lib.KIM_CanDeviceLockFrontPanel
KIM_CanDeviceLockFrontPanel.restype = c_bool
KIM_CanDeviceLockFrontPanel.argtypes = []


def can_device_lock_front_panel(serialNumber):
    '''
    Determine if the device front panel can be locked.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_CanDeviceLockFrontPanel(serialNumber)

    return output


KIM_CheckConnection = lib.KIM_CheckConnection
KIM_CheckConnection.restype = c_bool
KIM_CheckConnection.argtypes = [POINTER(c_char)]


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

    serialNumber = POINTER(c_char)()

    output = KIM_CheckConnection(serialNumber)

    return output


KIM_ClearMessageQueue = lib.KIM_ClearMessageQueue
KIM_ClearMessageQueue.restype = c_void_p
KIM_ClearMessageQueue.argtypes = []


def clear_message_queue(serialNumber):
    '''
    Clears the device message queue.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_ClearMessageQueue(serialNumber)

    return output


KIM_Close = lib.KIM_Close
KIM_Close.restype = c_void_p
KIM_Close.argtypes = []


def close_device(serialNumber):
    '''
    Disconnect and close the device.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_Close(serialNumber)

    return output


KIM_Disable = lib.KIM_Disable
KIM_Disable.restype = c_short
KIM_Disable.argtypes = []


def disable(serialNumber):
    '''
    Disable cube.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_Disable(serialNumber)

    return output


KIM_DisableChannel = lib.KIM_DisableChannel
KIM_DisableChannel.restype = c_short
KIM_DisableChannel.argtypes = []


def disable_channel(serialNumber):
    '''
    Disable a channel.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_DisableChannel(serialNumber)

    return output


KIM_Disconnect = lib.KIM_Disconnect
KIM_Disconnect.restype = c_short
KIM_Disconnect.argtypes = []


def disconnect(serialNumber):
    '''
    Tells the device that it is being disconnected.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_Disconnect(serialNumber)

    return output


KIM_Enable = lib.KIM_Enable
KIM_Enable.restype = c_short
KIM_Enable.argtypes = []


def enable(serialNumber):
    '''
    Enable cube for computer control.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_Enable(serialNumber)

    return output


KIM_EnableChannel = lib.KIM_EnableChannel
KIM_EnableChannel.restype = c_short
KIM_EnableChannel.argtypes = []


def enable_channel(serialNumber):
    '''
    Enable a channel.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_EnableChannel(serialNumber)

    return output


KIM_EnableLastMsgTimer = lib.KIM_EnableLastMsgTimer
KIM_EnableLastMsgTimer.restype = c_void_p
KIM_EnableLastMsgTimer.argtypes = []


def enable_last_msg_timer(serialNumber):
    '''
    Enables the last message monitoring timer.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        enable: c_bool
        lastMsgTimeout: c_int32

    Returns
    -------
        c_void_p
    '''

    serialNumber = POINTER(c_char)()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = KIM_EnableLastMsgTimer(serialNumber)

    return output


KIM_GetAbsoluteMoveParameters = lib.KIM_GetAbsoluteMoveParameters
KIM_GetAbsoluteMoveParameters.restype = c_short
KIM_GetAbsoluteMoveParameters.argtypes = []


def get_absolute_move_parameters(serialNumber):
    '''
    Gets a absolute move parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        absoluteMove: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    absoluteMove = c_int32()

    output = KIM_GetAbsoluteMoveParameters(serialNumber)

    return output


KIM_GetCurrentPosition = lib.KIM_GetCurrentPosition
KIM_GetCurrentPosition.restype = c_int32
KIM_GetCurrentPosition.argtypes = []


def get_current_position(serialNumber):
    '''
    Gets current position.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_int32
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_GetCurrentPosition(serialNumber)

    return output


KIM_GetDriveOPParameters = lib.KIM_GetDriveOPParameters
KIM_GetDriveOPParameters.restype = c_short
KIM_GetDriveOPParameters.argtypes = []


def get_drive_o_p_parameters(serialNumber):
    '''
    Gets the operation drive parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        maxVoltage: c_int16
        stepRate: c_int32
        stepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    maxVoltage = c_int16()
    stepRate = c_int32()
    stepAcceleration = c_int32()

    output = KIM_GetDriveOPParameters(serialNumber)

    return output


KIM_GetDriveOPParametersStruct = lib.KIM_GetDriveOPParametersStruct
KIM_GetDriveOPParametersStruct.restype = c_short
KIM_GetDriveOPParametersStruct.argtypes = []


def get_drive_o_p_parameters_struct(serialNumber):
    '''
    Gets the operation drive parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        driveOPParameters: KIM_DriveOPParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    driveOPParameters = KIM_DriveOPParameters()

    output = KIM_GetDriveOPParametersStruct(serialNumber)

    return output


KIM_GetFeedbackSigParameters = lib.KIM_GetFeedbackSigParameters
KIM_GetFeedbackSigParameters.restype = c_short
KIM_GetFeedbackSigParameters.argtypes = []


def get_feedback_sig_parameters(serialNumber):
    '''
    Gets a feedback signal parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        feedbackSignalMode: KIM_FBSignalMode
        encoderConst: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    feedbackSignalMode = KIM_FBSignalMode()
    encoderConst = c_int32()

    output = KIM_GetFeedbackSigParameters(serialNumber)

    return output


KIM_GetFeedbackSigParametersStruct = lib.KIM_GetFeedbackSigParametersStruct
KIM_GetFeedbackSigParametersStruct.restype = c_short
KIM_GetFeedbackSigParametersStruct.argtypes = []


def get_feedback_sig_parameters_struct(serialNumber):
    '''
    Gets a feedback signal parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        fbSigParameters: KIM_FeedbackSigParams

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    fbSigParameters = KIM_FeedbackSigParams()

    output = KIM_GetFeedbackSigParametersStruct(serialNumber)

    return output


KIM_GetFirmwareVersion = lib.KIM_GetFirmwareVersion
KIM_GetFirmwareVersion.restype = c_ulong
KIM_GetFirmwareVersion.argtypes = []


def get_firmware_version(serialNumber):
    '''
    Gets version number of the device firmware.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_GetFirmwareVersion(serialNumber)

    return output


KIM_GetFrontPanelLocked = lib.KIM_GetFrontPanelLocked
KIM_GetFrontPanelLocked.restype = c_bool
KIM_GetFrontPanelLocked.argtypes = []


def get_front_panel_locked(serialNumber):
    '''
    Query if the device front panel locked.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_GetFrontPanelLocked(serialNumber)

    return output


KIM_GetHardwareInfo = lib.KIM_GetHardwareInfo
KIM_GetHardwareInfo.restype = c_short
KIM_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    serialNumber = POINTER(c_char)()
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = KIM_GetHardwareInfo(serialNumber)

    return output


KIM_GetHardwareInfoBlock = lib.KIM_GetHardwareInfoBlock
KIM_GetHardwareInfoBlock.restype = c_short
KIM_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    serialNumber = POINTER(c_char)()
    hardwareInfo = TLI_HardwareInformation()

    output = KIM_GetHardwareInfoBlock(serialNumber)

    return output


KIM_GetHomeParameters = lib.KIM_GetHomeParameters
KIM_GetHomeParameters.restype = c_short
KIM_GetHomeParameters.argtypes = []


def get_home_parameters(serialNumber):
    '''
    Gets a home parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        homeDirection: KIM_TravelDirection
        homeLimitSwitch: KIM_TravelDirection
        homeStepRate: c_int32
        homeOffset: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    homeDirection = KIM_TravelDirection()
    homeLimitSwitch = KIM_TravelDirection()
    homeStepRate = c_int32()
    homeOffset = c_int32()

    output = KIM_GetHomeParameters(serialNumber)

    return output


KIM_GetHomeParametersStruct = lib.KIM_GetHomeParametersStruct
KIM_GetHomeParametersStruct.restype = c_short
KIM_GetHomeParametersStruct.argtypes = []


def get_home_parameters_struct(serialNumber):
    '''
    Gets a home parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        homeParameters: KIM_HomeParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    homeParameters = KIM_HomeParameters()

    output = KIM_GetHomeParametersStruct(serialNumber)

    return output


KIM_GetJogParameters = lib.KIM_GetJogParameters
KIM_GetJogParameters.restype = c_short
KIM_GetJogParameters.argtypes = []


def get_jog_parameters(serialNumber):
    '''
    Gets the jog parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        jogMode: KIM_JogMode
        jogStepSizeFwd: c_int32
        jogStepSizeRev: c_int32
        jogStepRate: c_int32
        jogStepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    jogMode = KIM_JogMode()
    jogStepSizeFwd = c_int32()
    jogStepSizeRev = c_int32()
    jogStepRate = c_int32()
    jogStepAcceleration = c_int32()

    output = KIM_GetJogParameters(serialNumber)

    return output


KIM_GetJogParametersStruct = lib.KIM_GetJogParametersStruct
KIM_GetJogParametersStruct.restype = c_short
KIM_GetJogParametersStruct.argtypes = []


def get_jog_parameters_struct(serialNumber):
    '''
    Gets the jog parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        jogParameters: KIM_JogParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    jogParameters = KIM_JogParameters()

    output = KIM_GetJogParametersStruct(serialNumber)

    return output


KIM_GetLimitSwitchParameters = lib.KIM_GetLimitSwitchParameters
KIM_GetLimitSwitchParameters.restype = c_short
KIM_GetLimitSwitchParameters.argtypes = []


def get_limit_switch_parameters(serialNumber):
    '''
    Gets a limit switch parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        forwardLimit: KIM_LimitSwitchModes
        reverseLimit: KIM_LimitSwitchModes
        stageID: c_int16

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    forwardLimit = KIM_LimitSwitchModes()
    reverseLimit = KIM_LimitSwitchModes()
    stageID = c_int16()

    output = KIM_GetLimitSwitchParameters(serialNumber)

    return output


KIM_GetLimitSwitchParametersStruct = lib.KIM_GetLimitSwitchParametersStruct
KIM_GetLimitSwitchParametersStruct.restype = c_short
KIM_GetLimitSwitchParametersStruct.argtypes = []


def get_limit_switch_parameters_struct(serialNumber):
    '''
    Gets a limit switch parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        limitSwitchParameters: KIM_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    limitSwitchParameters = KIM_LimitSwitchParameters()

    output = KIM_GetLimitSwitchParametersStruct(serialNumber)

    return output


KIM_GetMMIChannelParameters = lib.KIM_GetMMIChannelParameters
KIM_GetMMIChannelParameters.restype = c_short
KIM_GetMMIChannelParameters.argtypes = []


def get_m_m_i_channel_parameters(serialNumber):
    '''
    Gets a mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        presetPos1: c_int32
        presetPos2: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    presetPos1 = c_int32()
    presetPos2 = c_int32()

    output = KIM_GetMMIChannelParameters(serialNumber)

    return output


KIM_GetMMIChannelParametersStruct = lib.KIM_GetMMIChannelParametersStruct
KIM_GetMMIChannelParametersStruct.restype = c_short
KIM_GetMMIChannelParametersStruct.argtypes = []


def get_m_m_i_channel_parameters_struct(serialNumber):
    '''
    Gets a mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        mmiParameters: KIM_MMIChannelParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    mmiParameters = KIM_MMIChannelParameters()

    output = KIM_GetMMIChannelParametersStruct(serialNumber)

    return output


KIM_GetMMIDeviceParameters = lib.KIM_GetMMIDeviceParameters
KIM_GetMMIDeviceParameters.restype = c_short
KIM_GetMMIDeviceParameters.argtypes = []


def get_m_m_i_device_parameters(serialNumber):
    '''
    Gets a mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        joystickMode: KIM_JoysticModes
        maxStepRate: c_int32
        directionSense: KIM_DirectionSense
        presetPos1: c_int32
        presetPos2: c_int32
        displayIntensity: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    joystickMode = KIM_JoysticModes()
    maxStepRate = c_int32()
    directionSense = KIM_DirectionSense()
    presetPos1 = c_int32()
    presetPos2 = c_int32()
    displayIntensity = c_int32()

    output = KIM_GetMMIDeviceParameters(serialNumber)

    return output


KIM_GetMMIDeviceParametersStruct = lib.KIM_GetMMIDeviceParametersStruct
KIM_GetMMIDeviceParametersStruct.restype = c_short
KIM_GetMMIDeviceParametersStruct.argtypes = []


def get_m_m_i_device_parameters_struct(serialNumber):
    '''
    Gets a mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        mmiParameters: KIM_MMIParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    mmiParameters = KIM_MMIParameters()

    output = KIM_GetMMIDeviceParametersStruct(serialNumber)

    return output


KIM_GetNextMessage = lib.KIM_GetNextMessage
KIM_GetNextMessage.restype = c_bool
KIM_GetNextMessage.argtypes = []


def get_next_message(serialNumber):
    '''
    Get the next MessageQueue item.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = KIM_GetNextMessage(serialNumber)

    return output


KIM_GetRelativeMoveParameter = lib.KIM_GetRelativeMoveParameter
KIM_GetRelativeMoveParameter.restype = c_short
KIM_GetRelativeMoveParameter.argtypes = []


def get_relative_move_parameter(serialNumber):
    '''
    Gets a relative move parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        relativeMoveStep: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    relativeMoveStep = c_int32()

    output = KIM_GetRelativeMoveParameter(serialNumber)

    return output


KIM_GetSoftwareVersion = lib.KIM_GetSoftwareVersion
KIM_GetSoftwareVersion.restype = c_ulong
KIM_GetSoftwareVersion.argtypes = []


def get_software_version(serialNumber):
    '''
    Gets version number of the device software.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_GetSoftwareVersion(serialNumber)

    return output


KIM_GetStageType = lib.KIM_GetStageType
KIM_GetStageType.restype = KIM_Stages
KIM_GetStageType.argtypes = []


def get_stage_type(serialNumber):
    '''
    Gets the KIM stage type.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        KIM_Stages
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_GetStageType(serialNumber)

    return output


KIM_GetStatusBits = lib.KIM_GetStatusBits
KIM_GetStatusBits.restype = c_ulong
KIM_GetStatusBits.argtypes = []


def get_status_bits(serialNumber):
    '''
    Tc get status bits.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_ulong
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_GetStatusBits(serialNumber)

    return output


KIM_GetTrigIOParameters = lib.KIM_GetTrigIOParameters
KIM_GetTrigIOParameters.restype = c_short
KIM_GetTrigIOParameters.argtypes = []


def get_trig_i_o_parameters(serialNumber):
    '''
    Gets a trig IO parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        trig1Mode: KIM_TrigModes
        trig1Polarity: KIM_TrigPolarities
        trigChannel1: KIM_Channels
        trig2Mode: KIM_TrigModes
        trig2Polarity: KIM_TrigPolarities
        trigChannel2: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    trig1Mode = KIM_TrigModes()
    trig1Polarity = KIM_TrigPolarities()
    trigChannel1 = KIM_Channels()
    trig2Mode = KIM_TrigModes()
    trig2Polarity = KIM_TrigPolarities()
    trigChannel2 = KIM_Channels()

    output = KIM_GetTrigIOParameters(serialNumber)

    return output


KIM_GetTrigIOParametersStruct = lib.KIM_GetTrigIOParametersStruct
KIM_GetTrigIOParametersStruct.restype = c_short
KIM_GetTrigIOParametersStruct.argtypes = []


def get_trig_i_o_parameters_struct(serialNumber):
    '''
    Gets a trig IO parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        trigIOParameters: KIM_TrigIOConfig

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    trigIOParameters = KIM_TrigIOConfig()

    output = KIM_GetTrigIOParametersStruct(serialNumber)

    return output


KIM_GetTrigParamsParameters = lib.KIM_GetTrigParamsParameters
KIM_GetTrigParamsParameters.restype = c_short
KIM_GetTrigParamsParameters.argtypes = []


def get_trig_params_parameters(serialNumber):
    '''
    Gets a trigger parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        startPosFwd: c_int32
        intervalFwd: c_int32
        numberOfPulsesFwd: c_int32
        startPosRev: c_int32
        intervalRev: c_int32
        numberOfPulsesRev: c_int32
        pulseWidth: c_int32
        numberOfCycles: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    startPosFwd = c_int32()
    intervalFwd = c_int32()
    numberOfPulsesFwd = c_int32()
    startPosRev = c_int32()
    intervalRev = c_int32()
    numberOfPulsesRev = c_int32()
    pulseWidth = c_int32()
    numberOfCycles = c_int32()

    output = KIM_GetTrigParamsParameters(serialNumber)

    return output


KIM_GetTrigParamsParametersStruct = lib.KIM_GetTrigParamsParametersStruct
KIM_GetTrigParamsParametersStruct.restype = c_short
KIM_GetTrigParamsParametersStruct.argtypes = []


def get_trig_params_parameters_struct(serialNumber):
    '''
    Gets a trigger parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        trigParameters: KIM_TrigParamsParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    trigParameters = KIM_TrigParamsParameters()

    output = KIM_GetTrigParamsParametersStruct(serialNumber)

    return output


KIM_HasLastMsgTimerOverrun = lib.KIM_HasLastMsgTimerOverrun
KIM_HasLastMsgTimerOverrun.restype = c_bool
KIM_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serialNumber):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by KIM_EnableLastMsgTimer(char const * serialNumber, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_HasLastMsgTimerOverrun(serialNumber)

    return output


KIM_Home = lib.KIM_Home
KIM_Home.restype = c_short
KIM_Home.argtypes = []


def home(serialNumber):
    '''
    Home the device to a limit switch or reset to zero if no limit switches available.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_Home(serialNumber)

    return output


KIM_Identify = lib.KIM_Identify
KIM_Identify.restype = c_void_p
KIM_Identify.argtypes = []


def identify(serialNumber):
    '''
    Sends a command to the device to make it identify iteself.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_Identify(serialNumber)

    return output


KIM_IsDualChannelMode = lib.KIM_IsDualChannelMode
KIM_IsDualChannelMode.restype = c_bool
KIM_IsDualChannelMode.argtypes = []


def is_dual_channel_mode(serialNumber):
    '''
    Gets the Dual Channel Mode state.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_IsDualChannelMode(serialNumber)

    return output


KIM_LoadNamedSettings = lib.KIM_LoadNamedSettings
KIM_LoadNamedSettings.restype = c_bool
KIM_LoadNamedSettings.argtypes = []


def load_named_settings(serialNumber):
    '''
    Update device with named settings.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        settingsName: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()
    settingsName = POINTER(c_char)()

    output = KIM_LoadNamedSettings(serialNumber)

    return output


KIM_LoadSettings = lib.KIM_LoadSettings
KIM_LoadSettings.restype = c_bool
KIM_LoadSettings.argtypes = []


def load_settings(serialNumber):
    '''
    Update device with stored settings.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_LoadSettings(serialNumber)

    return output


KIM_MessageQueueSize = lib.KIM_MessageQueueSize
KIM_MessageQueueSize.restype = c_int
KIM_MessageQueueSize.argtypes = []


def message_queue_size(serialNumber):
    '''
    Gets the MessageQueue size.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_MessageQueueSize(serialNumber)

    return output


KIM_MoveAbsolute = lib.KIM_MoveAbsolute
KIM_MoveAbsolute.restype = c_short
KIM_MoveAbsolute.argtypes = []


def move_absolute(serialNumber):
    '''
    Move absolute.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        position: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    position = c_int32()

    output = KIM_MoveAbsolute(serialNumber)

    return output


KIM_MoveJog = lib.KIM_MoveJog
KIM_MoveJog.restype = c_short
KIM_MoveJog.argtypes = []


def move_jog(serialNumber):
    '''
    Move jog.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        jogDirection: KIM_TravelDirection

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    jogDirection = KIM_TravelDirection()

    output = KIM_MoveJog(serialNumber)

    return output


KIM_MoveRelative = lib.KIM_MoveRelative
KIM_MoveRelative.restype = c_short
KIM_MoveRelative.argtypes = []


def move_relative(serialNumber):
    '''
    Move relative.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        stepSize: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    stepSize = c_int32()

    output = KIM_MoveRelative(serialNumber)

    return output


KIM_MoveStop = lib.KIM_MoveStop
KIM_MoveStop.restype = c_short
KIM_MoveStop.argtypes = []


def move_stop(serialNumber):
    '''
    Move stop.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_MoveStop(serialNumber)

    return output


KIM_Open = lib.KIM_Open
KIM_Open.restype = c_short
KIM_Open.argtypes = []


def open_device(serialNumber):
    '''
    Open the device for communications.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_Open(serialNumber)

    return output


KIM_PersistSettings = lib.KIM_PersistSettings
KIM_PersistSettings.restype = c_bool
KIM_PersistSettings.argtypes = []


def persist_settings(serialNumber):
    '''
    persist the devices current settings.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_PersistSettings(serialNumber)

    return output


KIM_PollingDuration = lib.KIM_PollingDuration
KIM_PollingDuration.restype = c_long
KIM_PollingDuration.argtypes = []


def polling_duration(serialNumber):
    '''
    Gets the polling loop duration.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_PollingDuration(serialNumber)

    return output


KIM_RegisterMessageCallback = lib.KIM_RegisterMessageCallback
KIM_RegisterMessageCallback.restype = c_void_p
KIM_RegisterMessageCallback.argtypes = []


def register_message_callback(serialNumber):
    '''
    Registers a callback on the message queue.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        None

    Returns
    -------
        c_void_p
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_RegisterMessageCallback(serialNumber)

    return output


KIM_RequestAbsoluteMoveParameters = lib.KIM_RequestAbsoluteMoveParameters
KIM_RequestAbsoluteMoveParameters.restype = c_short
KIM_RequestAbsoluteMoveParameters.argtypes = []


def request_absolute_move_parameters(serialNumber):
    '''
    Request the absolute move parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestAbsoluteMoveParameters(serialNumber)

    return output


KIM_RequestCurrentPosition = lib.KIM_RequestCurrentPosition
KIM_RequestCurrentPosition.restype = c_short
KIM_RequestCurrentPosition.argtypes = []


def request_current_position(serialNumber):
    '''
    Requests the current position.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestCurrentPosition(serialNumber)

    return output


KIM_RequestDriveOPParameters = lib.KIM_RequestDriveOPParameters
KIM_RequestDriveOPParameters.restype = c_short
KIM_RequestDriveOPParameters.argtypes = []


def request_drive_o_p_parameters(serialNumber):
    '''
    Requests the operation drive parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestDriveOPParameters(serialNumber)

    return output


KIM_RequestFeedbackSigParameters = lib.KIM_RequestFeedbackSigParameters
KIM_RequestFeedbackSigParameters.restype = c_short
KIM_RequestFeedbackSigParameters.argtypes = []


def request_feedback_sig_parameters(serialNumber):
    '''
    Request the feedback signal parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestFeedbackSigParameters(serialNumber)

    return output


KIM_RequestFrontPanelLocked = lib.KIM_RequestFrontPanelLocked
KIM_RequestFrontPanelLocked.restype = c_short
KIM_RequestFrontPanelLocked.argtypes = []


def request_front_panel_locked(serialNumber):
    '''
    Ask the device if its front panel is locked.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_RequestFrontPanelLocked(serialNumber)

    return output


KIM_RequestHomeParameters = lib.KIM_RequestHomeParameters
KIM_RequestHomeParameters.restype = c_short
KIM_RequestHomeParameters.argtypes = []


def request_home_parameters(serialNumber):
    '''
    Request the home parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestHomeParameters(serialNumber)

    return output


KIM_RequestJogParameters = lib.KIM_RequestJogParameters
KIM_RequestJogParameters.restype = c_short
KIM_RequestJogParameters.argtypes = []


def request_jog_parameters(serialNumber):
    '''
    Requests the jog parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestJogParameters(serialNumber)

    return output


KIM_RequestLimitSwitchParameters = lib.KIM_RequestLimitSwitchParameters
KIM_RequestLimitSwitchParameters.restype = c_short
KIM_RequestLimitSwitchParameters.argtypes = []


def request_limit_switch_parameters(serialNumber):
    '''
    Request the limit switch parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestLimitSwitchParameters(serialNumber)

    return output


KIM_RequestMMIParameters = lib.KIM_RequestMMIParameters
KIM_RequestMMIParameters.restype = c_short
KIM_RequestMMIParameters.argtypes = []


def request_m_m_i_parameters(serialNumber):
    '''
    Request the mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestMMIParameters(serialNumber)

    return output


KIM_RequestRelativeMoveParameter = lib.KIM_RequestRelativeMoveParameter
KIM_RequestRelativeMoveParameter.restype = c_short
KIM_RequestRelativeMoveParameter.argtypes = []


def request_relative_move_parameter(serialNumber):
    '''
    Request the relative move parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestRelativeMoveParameter(serialNumber)

    return output


KIM_RequestSettings = lib.KIM_RequestSettings
KIM_RequestSettings.restype = c_short
KIM_RequestSettings.argtypes = []


def request_settings(serialNumber):
    '''
    Requests that all settings are download from device.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_RequestSettings(serialNumber)

    return output


KIM_RequestStageType = lib.KIM_RequestStageType
KIM_RequestStageType.restype = c_short
KIM_RequestStageType.argtypes = []


def request_stage_type(serialNumber):
    '''
    Request KIM stage type.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_RequestStageType(serialNumber)

    return output


KIM_RequestStatus = lib.KIM_RequestStatus
KIM_RequestStatus.restype = c_short
KIM_RequestStatus.argtypes = []


def request_status(serialNumber):
    '''
    Requests the state quantities (actual temperature, current and status bits).

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_RequestStatus(serialNumber)

    return output


KIM_RequestStatusBits = lib.KIM_RequestStatusBits
KIM_RequestStatusBits.restype = c_short
KIM_RequestStatusBits.argtypes = []


def request_status_bits(serialNumber):
    '''
    Request the status bits which identify the current device state.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_RequestStatusBits(serialNumber)

    return output


KIM_RequestTrigIOParameters = lib.KIM_RequestTrigIOParameters
KIM_RequestTrigIOParameters.restype = c_short
KIM_RequestTrigIOParameters.argtypes = []


def request_trig_i_o_parameters(serialNumber):
    '''
    Request the trig IO parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_RequestTrigIOParameters(serialNumber)

    return output


KIM_RequestTrigParamsParameters = lib.KIM_RequestTrigParamsParameters
KIM_RequestTrigParamsParameters.restype = c_short
KIM_RequestTrigParamsParameters.argtypes = []


def request_trig_params_parameters(serialNumber):
    '''
    Request the trigger parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_RequestTrigParamsParameters(serialNumber)

    return output


KIM_Reset = lib.KIM_Reset
KIM_Reset.restype = c_short
KIM_Reset.argtypes = []


def reset(serialNumber):
    '''
    Reset the device.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_Reset(serialNumber)

    return output


KIM_SetAbsoluteMoveParameters = lib.KIM_SetAbsoluteMoveParameters
KIM_SetAbsoluteMoveParameters.restype = c_short
KIM_SetAbsoluteMoveParameters.argtypes = []


def set_absolute_move_parameters(serialNumber):
    '''
    Sets the absolute move parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        absoluteMove: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    absoluteMove = c_int32()

    output = KIM_SetAbsoluteMoveParameters(serialNumber)

    return output


KIM_SetDriveOPParameters = lib.KIM_SetDriveOPParameters
KIM_SetDriveOPParameters.restype = c_short
KIM_SetDriveOPParameters.argtypes = []


def set_drive_o_p_parameters(serialNumber):
    '''
    Sets the operation drive parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        maxVoltage: c_int16
        stepRate: c_int32
        stepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    maxVoltage = c_int16()
    stepRate = c_int32()
    stepAcceleration = c_int32()

    output = KIM_SetDriveOPParameters(serialNumber)

    return output


KIM_SetDriveOPParametersStruct = lib.KIM_SetDriveOPParametersStruct
KIM_SetDriveOPParametersStruct.restype = c_short
KIM_SetDriveOPParametersStruct.argtypes = []


def set_drive_o_p_parameters_struct(serialNumber):
    '''
    Sets the operation drive parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        driveOPParameters: KIM_DriveOPParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    driveOPParameters = KIM_DriveOPParameters()

    output = KIM_SetDriveOPParametersStruct(serialNumber)

    return output


KIM_SetDualChannelMode = lib.KIM_SetDualChannelMode
KIM_SetDualChannelMode.restype = c_short
KIM_SetDualChannelMode.argtypes = []


def set_dual_channel_mode(serialNumber):
    '''
    Sets the Dual Channel Mode.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        enableDualChannel: c_bool

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    enableDualChannel = c_bool()

    output = KIM_SetDualChannelMode(serialNumber)

    return output


KIM_SetFeedbackSigParameters = lib.KIM_SetFeedbackSigParameters
KIM_SetFeedbackSigParameters.restype = c_short
KIM_SetFeedbackSigParameters.argtypes = []


def set_feedback_sig_parameters(serialNumber):
    '''
    Sets the feedback signal parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        feedbackSignalMode: KIM_FBSignalMode
        encoderConst: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    feedbackSignalMode = KIM_FBSignalMode()
    encoderConst = c_int32()

    output = KIM_SetFeedbackSigParameters(serialNumber)

    return output


KIM_SetFeedbackSigParametersStruct = lib.KIM_SetFeedbackSigParametersStruct
KIM_SetFeedbackSigParametersStruct.restype = c_short
KIM_SetFeedbackSigParametersStruct.argtypes = []


def set_feedback_sig_parameters_struct(serialNumber):
    '''
    Sets the feedback signal parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        fbSigParameters: KIM_FeedbackSigParams

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    fbSigParameters = KIM_FeedbackSigParams()

    output = KIM_SetFeedbackSigParametersStruct(serialNumber)

    return output


KIM_SetFrontPanelLock = lib.KIM_SetFrontPanelLock
KIM_SetFrontPanelLock.restype = c_short
KIM_SetFrontPanelLock.argtypes = []


def set_front_panel_lock(serialNumber):
    '''
    Sets the device front panel lock state.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        locked: c_bool

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    locked = c_bool()

    output = KIM_SetFrontPanelLock(serialNumber)

    return output


KIM_SetHomeParameters = lib.KIM_SetHomeParameters
KIM_SetHomeParameters.restype = c_short
KIM_SetHomeParameters.argtypes = []


def set_home_parameters(serialNumber):
    '''
    Sets the home parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        homeDirection: KIM_TravelDirection
        homeLimitSwitch: KIM_TravelDirection
        homeStepRate: c_int32
        homeOffset: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    homeDirection = KIM_TravelDirection()
    homeLimitSwitch = KIM_TravelDirection()
    homeStepRate = c_int32()
    homeOffset = c_int32()

    output = KIM_SetHomeParameters(serialNumber)

    return output


KIM_SetHomeParametersStruct = lib.KIM_SetHomeParametersStruct
KIM_SetHomeParametersStruct.restype = c_short
KIM_SetHomeParametersStruct.argtypes = []


def set_home_parameters_struct(serialNumber):
    '''
    Sets the home parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        homeParameters: KIM_HomeParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    homeParameters = KIM_HomeParameters()

    output = KIM_SetHomeParametersStruct(serialNumber)

    return output


KIM_SetJogParameters = lib.KIM_SetJogParameters
KIM_SetJogParameters.restype = c_short
KIM_SetJogParameters.argtypes = []


def set_jog_parameters(serialNumber):
    '''
    Sets the jog parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        jogMode: KIM_JogMode
        jogStepSizeFwd: c_int32
        jogStepSizeRev: c_int32
        jogStepRate: c_int32
        jogStepAcceleration: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    jogMode = KIM_JogMode()
    jogStepSizeFwd = c_int32()
    jogStepSizeRev = c_int32()
    jogStepRate = c_int32()
    jogStepAcceleration = c_int32()

    output = KIM_SetJogParameters(serialNumber)

    return output


KIM_SetJogParametersStruct = lib.KIM_SetJogParametersStruct
KIM_SetJogParametersStruct.restype = c_short
KIM_SetJogParametersStruct.argtypes = []


def set_jog_parameters_struct(serialNumber):
    '''
    Sets the jog parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        jogParameters: KIM_JogParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    jogParameters = KIM_JogParameters()

    output = KIM_SetJogParametersStruct(serialNumber)

    return output


KIM_SetLimitSwitchParameters = lib.KIM_SetLimitSwitchParameters
KIM_SetLimitSwitchParameters.restype = c_short
KIM_SetLimitSwitchParameters.argtypes = []


def set_limit_switch_parameters(serialNumber):
    '''
    Sets the limit switch parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        forwardLimit: KIM_LimitSwitchModes
        reverseLimit: KIM_LimitSwitchModes
        stageID: c_int16

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    forwardLimit = KIM_LimitSwitchModes()
    reverseLimit = KIM_LimitSwitchModes()
    stageID = c_int16()

    output = KIM_SetLimitSwitchParameters(serialNumber)

    return output


KIM_SetLimitSwitchParametersStruct = lib.KIM_SetLimitSwitchParametersStruct
KIM_SetLimitSwitchParametersStruct.restype = c_short
KIM_SetLimitSwitchParametersStruct.argtypes = []


def set_limit_switch_parameters_struct(serialNumber):
    '''
    Sets the limit switch parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        limitSwitchParameters: KIM_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    limitSwitchParameters = KIM_LimitSwitchParameters()

    output = KIM_SetLimitSwitchParametersStruct(serialNumber)

    return output


KIM_SetMMIChannelParameters = lib.KIM_SetMMIChannelParameters
KIM_SetMMIChannelParameters.restype = c_short
KIM_SetMMIChannelParameters.argtypes = []


def set_m_m_i_channel_parameters(serialNumber):
    '''
    Sets the mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        presetPos1: c_int32
        presetPos2: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    presetPos1 = c_int32()
    presetPos2 = c_int32()

    output = KIM_SetMMIChannelParameters(serialNumber)

    return output


KIM_SetMMIChannelParametersStruct = lib.KIM_SetMMIChannelParametersStruct
KIM_SetMMIChannelParametersStruct.restype = c_short
KIM_SetMMIChannelParametersStruct.argtypes = []


def set_m_m_i_channel_parameters_struct(serialNumber):
    '''
    Sets the mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        mmiParameters: KIM_MMIChannelParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    mmiParameters = KIM_MMIChannelParameters()

    output = KIM_SetMMIChannelParametersStruct(serialNumber)

    return output


KIM_SetMMIDeviceParameters = lib.KIM_SetMMIDeviceParameters
KIM_SetMMIDeviceParameters.restype = c_short
KIM_SetMMIDeviceParameters.argtypes = []


def set_m_m_i_device_parameters(serialNumber):
    '''
    Sets the mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        joystickMode: KIM_JoysticModes
        maxStepRate: c_int32
        directionSense: KIM_DirectionSense
        displayIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    joystickMode = KIM_JoysticModes()
    maxStepRate = c_int32()
    directionSense = KIM_DirectionSense()
    displayIntensity = c_int16()

    output = KIM_SetMMIDeviceParameters(serialNumber)

    return output


KIM_SetMMIDeviceParametersStruct = lib.KIM_SetMMIDeviceParametersStruct
KIM_SetMMIDeviceParametersStruct.restype = c_short
KIM_SetMMIDeviceParametersStruct.argtypes = []


def set_m_m_i_device_parameters_struct(serialNumber):
    '''
    Sets the mmi parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        mmiParameters: KIM_MMIParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    mmiParameters = KIM_MMIParameters()

    output = KIM_SetMMIDeviceParametersStruct(serialNumber)

    return output


KIM_SetPosition = lib.KIM_SetPosition
KIM_SetPosition.restype = c_short
KIM_SetPosition.argtypes = []


def set_position(serialNumber):
    '''
    set the position.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        position: c_long

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    position = c_long()

    output = KIM_SetPosition(serialNumber)

    return output


KIM_SetRelativeMoveParameter = lib.KIM_SetRelativeMoveParameter
KIM_SetRelativeMoveParameter.restype = c_short
KIM_SetRelativeMoveParameter.argtypes = []


def set_relative_move_parameter(serialNumber):
    '''
    Sets the relative move parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        relativeMove: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    relativeMove = c_int32()

    output = KIM_SetRelativeMoveParameter(serialNumber)

    return output


KIM_SetStageType = lib.KIM_SetStageType
KIM_SetStageType.restype = c_short
KIM_SetStageType.argtypes = []


def set_stage_type(serialNumber):
    '''
    Sets the KIM stage type.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        stageType: KIM_Stages

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    stageType = KIM_Stages()

    output = KIM_SetStageType(serialNumber)

    return output


KIM_SetTrigIOParameters = lib.KIM_SetTrigIOParameters
KIM_SetTrigIOParameters.restype = c_short
KIM_SetTrigIOParameters.argtypes = []


def set_trig_i_o_parameters(serialNumber):
    '''
    Sets the limit switch parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        trig1Mode: KIM_TrigModes
        trig1Polarity: KIM_TrigPolarities
        trigChannel1: KIM_Channels
        trig2Mode: KIM_TrigModes
        trig2Polarity: KIM_TrigPolarities
        trigChannel2: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    trig1Mode = KIM_TrigModes()
    trig1Polarity = KIM_TrigPolarities()
    trigChannel1 = KIM_Channels()
    trig2Mode = KIM_TrigModes()
    trig2Polarity = KIM_TrigPolarities()
    trigChannel2 = KIM_Channels()

    output = KIM_SetTrigIOParameters(serialNumber)

    return output


KIM_SetTrigIOParametersStruct = lib.KIM_SetTrigIOParametersStruct
KIM_SetTrigIOParametersStruct.restype = c_short
KIM_SetTrigIOParametersStruct.argtypes = []


def set_trig_i_o_parameters_struct(serialNumber):
    '''
    Sets the limit switch parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        trigIOParameters: KIM_TrigIOConfig

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    trigIOParameters = KIM_TrigIOConfig()

    output = KIM_SetTrigIOParametersStruct(serialNumber)

    return output


KIM_SetTrigParamsParameters = lib.KIM_SetTrigParamsParameters
KIM_SetTrigParamsParameters.restype = c_short
KIM_SetTrigParamsParameters.argtypes = []


def set_trig_params_parameters(serialNumber):
    '''
    Sets the trigger parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        trigParameters: KIM_TrigParamsParameters
        startPosFwd: c_int32
        intervalFwd: c_int32
        numberOfPulsesFwd: c_int32
        startPosRev: c_int32
        intervalRev: c_int32
        numberOfPulsesRev: c_int32
        pulseWidth: c_int32
        numberOfCycles: c_int32

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    trigParameters = KIM_TrigParamsParameters()
    startPosFwd = c_int32()
    intervalFwd = c_int32()
    numberOfPulsesFwd = c_int32()
    startPosRev = c_int32()
    intervalRev = c_int32()
    numberOfPulsesRev = c_int32()
    pulseWidth = c_int32()
    numberOfCycles = c_int32()

    output = KIM_SetTrigParamsParameters(serialNumber)

    return output


KIM_SetTrigParamsParametersStruct = lib.KIM_SetTrigParamsParametersStruct
KIM_SetTrigParamsParametersStruct.restype = c_short
KIM_SetTrigParamsParametersStruct.argtypes = []


def set_trig_params_parameters_struct(serialNumber):
    '''
    Sets the trigger parameters.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels
        trigParameters: KIM_TrigParamsParameters

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()
    trigParameters = KIM_TrigParamsParameters()

    output = KIM_SetTrigParamsParametersStruct(serialNumber)

    return output


KIM_StartPolling = lib.KIM_StartPolling
KIM_StartPolling.restype = c_bool
KIM_StartPolling.argtypes = []


def start_polling(serialNumber):
    '''
    Starts the internal polling loop which continuously requests position and status.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        milliseconds: c_int

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()
    milliseconds = c_int()

    output = KIM_StartPolling(serialNumber)

    return output


KIM_StopPolling = lib.KIM_StopPolling
KIM_StopPolling.restype = c_void_p
KIM_StopPolling.argtypes = []


def stop_polling(serialNumber):
    '''
    Stops the internal polling loop.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_StopPolling(serialNumber)

    return output


KIM_SupportsDualChannelMode = lib.KIM_SupportsDualChannelMode
KIM_SupportsDualChannelMode.restype = c_bool
KIM_SupportsDualChannelMode.argtypes = []


def supports_dual_channel_mode(serialNumber):
    '''
    Determines whether the device supports Dual Channel Mode.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_SupportsDualChannelMode(serialNumber)

    return output


KIM_SupportsStageType = lib.KIM_SupportsStageType
KIM_SupportsStageType.restype = c_bool
KIM_SupportsStageType.argtypes = []


def supports_stage_type(serialNumber):
    '''
    Gets a flag to show whether the KIM stage type is supported.

    Parameters
    ----------
        serialNumber: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()

    output = KIM_SupportsStageType(serialNumber)

    return output


KIM_TimeSinceLastMsgReceived = lib.KIM_TimeSinceLastMsgReceived
KIM_TimeSinceLastMsgReceived.restype = c_bool
KIM_TimeSinceLastMsgReceived.argtypes = []


def time_since_last_msg_received(serialNumber):
    '''
    Gets the time in milliseconds since tha last message was received from the device.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        lastUpdateTimeMS: c_int64

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()
    lastUpdateTimeMS = c_int64()

    output = KIM_TimeSinceLastMsgReceived(serialNumber)

    return output


KIM_WaitForMessage = lib.KIM_WaitForMessage
KIM_WaitForMessage.restype = c_bool
KIM_WaitForMessage.argtypes = []


def wait_for_message(serialNumber):
    '''
    Wait for next MessageQueue item.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serialNumber = POINTER(c_char)()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = KIM_WaitForMessage(serialNumber)

    return output


KIM_ZeroPosition = lib.KIM_ZeroPosition
KIM_ZeroPosition.restype = c_short
KIM_ZeroPosition.argtypes = []


def zero_position(serialNumber):
    '''
    Sets the current position to zero.

    Parameters
    ----------
        serialNumber: POINTER(c_char)
        channel: KIM_Channels

    Returns
    -------
        c_short
    '''

    serialNumber = POINTER(c_char)()
    channel = KIM_Channels()

    output = KIM_ZeroPosition(serialNumber)

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



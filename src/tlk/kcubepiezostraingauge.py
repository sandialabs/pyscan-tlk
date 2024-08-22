from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_int,
    c_int16,
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
    KPC_HubAnalogueModes,
    KPC_IOSettings,
    KPC_MonitorOutputMode,
    KPC_TriggerPortMode,
    KPC_TriggerPortPolarity,
    KPZ_WheelChangeRate,
    KPZ_WheelDirectionSense,
    KPZ_WheelMode,
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
    KPC_MMIParams,
    KPC_TriggerConfig,
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.PiezoStrainGauge.DLL")

KPC_CanDeviceLockFrontPanel = lib.KPC_CanDeviceLockFrontPanel
KPC_CanDeviceLockFrontPanel.restype = c_bool
KPC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


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

    output = KPC_CanDeviceLockFrontPanel(serial_number)

    return output


KPC_CheckConnection = lib.KPC_CheckConnection
KPC_CheckConnection.restype = c_bool
KPC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = KPC_CheckConnection(serial_number)

    return output


KPC_ClearMessageQueue = lib.KPC_ClearMessageQueue
KPC_ClearMessageQueue.restype = c_void_p
KPC_ClearMessageQueue.argtypes = [POINTER(c_char)]


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

    output = KPC_ClearMessageQueue(serial_number)

    return output


KPC_Close = lib.KPC_Close
KPC_Close.restype = c_void_p
KPC_Close.argtypes = [POINTER(c_char)]


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

    output = KPC_Close(serial_number)

    return output


KPC_Disable = lib.KPC_Disable
KPC_Disable.restype = c_short
KPC_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    '''
    Disable the cube.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_Disable(serial_number)

    return output


KPC_Disconnect = lib.KPC_Disconnect
KPC_Disconnect.restype = c_short
KPC_Disconnect.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_Disconnect(serial_number)

    return output


KPC_Enable = lib.KPC_Enable
KPC_Enable.restype = c_short
KPC_Enable.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_Enable(serial_number)

    return output


KPC_EnableLastMsgTimer = lib.KPC_EnableLastMsgTimer
KPC_EnableLastMsgTimer.restype = c_void_p
KPC_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


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

    output = KPC_EnableLastMsgTimer(serial_number)

    return output


KPC_GetDigitalOutputs = lib.KPC_GetDigitalOutputs
KPC_GetDigitalOutputs.restype = c_byte
KPC_GetDigitalOutputs.argtypes = [POINTER(c_char)]


def get_digital_outputs(serial_number):
    '''
    Gets the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetDigitalOutputs(serial_number)

    return output


KPC_GetFeedbackLoopPIconsts = lib.KPC_GetFeedbackLoopPIconsts
KPC_GetFeedbackLoopPIconsts.restype = c_short
KPC_GetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def get_feedback_loop_p_iconsts(serial_number):
    '''
    Gets the feedback loop constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalTerm: c_short
        integralTerm: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = KPC_GetFeedbackLoopPIconsts(serial_number)

    return output


KPC_GetFeedbackLoopPIconstsBlock = lib.KPC_GetFeedbackLoopPIconstsBlock
KPC_GetFeedbackLoopPIconstsBlock.restype = c_short
KPC_GetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


def get_feedback_loop_p_iconsts_block(serial_number):
    '''
    Gets the feedback loop constants in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalAndIntegralConstants: PZ_FeedbackLoopConstants

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = KPC_GetFeedbackLoopPIconstsBlock(serial_number)

    return output


KPC_GetFirmwareVersion = lib.KPC_GetFirmwareVersion
KPC_GetFirmwareVersion.restype = c_ulong
KPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


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

    output = KPC_GetFirmwareVersion(serial_number)

    return output


KPC_GetFrontPanelLocked = lib.KPC_GetFrontPanelLocked
KPC_GetFrontPanelLocked.restype = c_bool
KPC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


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

    output = KPC_GetFrontPanelLocked(serial_number)

    return output


KPC_GetHardwareInfo = lib.KPC_GetHardwareInfo
KPC_GetHardwareInfo.restype = c_short
KPC_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = KPC_GetHardwareInfo(serial_number)

    return output


KPC_GetHardwareInfoBlock = lib.KPC_GetHardwareInfoBlock
KPC_GetHardwareInfoBlock.restype = c_short
KPC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = KPC_GetHardwareInfoBlock(serial_number)

    return output


KPC_GetHardwareMaxOutputVoltage = lib.KPC_GetHardwareMaxOutputVoltage
KPC_GetHardwareMaxOutputVoltage.restype = c_short
KPC_GetHardwareMaxOutputVoltage.argtypes = [POINTER(c_char)]


def get_hardware_max_output_voltage(serial_number):
    '''
    Gets the hardware maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetHardwareMaxOutputVoltage(serial_number)

    return output


KPC_GetHubAnalogInput = lib.KPC_GetHubAnalogInput
KPC_GetHubAnalogInput.restype = KPC_HubAnalogueModes
KPC_GetHubAnalogInput.argtypes = [POINTER(c_char)]


def get_hub_analog_input(serial_number):
    '''
    Gets the Hub Analog Input.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        KPC_HubAnalogueModes
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetHubAnalogInput(serial_number)

    return output


KPC_GetIOSettings = lib.KPC_GetIOSettings
KPC_GetIOSettings.restype = KPC_IOSettings
KPC_GetIOSettings.argtypes = [POINTER(c_char)]


def get_i_o_settings(serial_number):
    '''
    Gets the IO settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        KPC_IOSettings
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetIOSettings(serial_number)

    return output


KPC_GetLEDBrightness = lib.KPC_GetLEDBrightness
KPC_GetLEDBrightness.restype = c_short
KPC_GetLEDBrightness.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetLEDBrightness(serial_number)

    return output


KPC_GetMMIParams = lib.KPC_GetMMIParams
KPC_GetMMIParams.restype = c_short
KPC_GetMMIParams.argtypes = [POINTER(c_char)]


def get_m_m_i_params(serial_number):
    '''
    Get the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KPZ_WheelMode
        voltageAdjustRate: KPZ_WheelChangeRate
        voltageStep: c_int16
        positionStep: c_int16
        directionSense: KPZ_WheelDirectionSense
        presetVoltage1: c_int16
        presetVoltage2: c_int16
        presetPosition1: c_int16
        presetPosition2: c_int16
        displayIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int16()
    positionStep = c_int16()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int16()
    presetVoltage2 = c_int16()
    presetPosition1 = c_int16()
    presetPosition2 = c_int16()
    displayIntensity = c_int16()

    output = KPC_GetMMIParams(serial_number)

    return output


KPC_GetMMIParamsBlock = lib.KPC_GetMMIParamsBlock
KPC_GetMMIParamsBlock.restype = c_short
KPC_GetMMIParamsBlock.argtypes = [POINTER(c_char)]


def get_m_m_i_params_block(serial_number):
    '''
    Gets the MMI parameters for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mmiParams: KPC_MMIParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mmiParams = KPC_MMIParams()

    output = KPC_GetMMIParamsBlock(serial_number)

    return output


KPC_GetMMIParamsExt = lib.KPC_GetMMIParamsExt
KPC_GetMMIParamsExt.restype = c_short
KPC_GetMMIParamsExt.argtypes = [POINTER(c_char)]


def get_m_m_i_params_ext(serial_number):
    '''
    Get the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KPZ_WheelMode
        voltageAdjustRate: KPZ_WheelChangeRate
        voltageStep: c_int16
        positionStep: c_int16
        directionSense: KPZ_WheelDirectionSense
        presetVoltage1: c_int16
        presetVoltage2: c_int16
        presetPosition1: c_int16
        presetPosition2: c_int16
        displayIntensity: c_int16
        displayTimeout: c_int16
        displayDimIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int16()
    positionStep = c_int16()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int16()
    presetVoltage2 = c_int16()
    presetPosition1 = c_int16()
    presetPosition2 = c_int16()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = KPC_GetMMIParamsExt(serial_number)

    return output


KPC_GetMaxOutputVoltage = lib.KPC_GetMaxOutputVoltage
KPC_GetMaxOutputVoltage.restype = c_short
KPC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def get_max_output_voltage(serial_number):
    '''
    Gets the maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetMaxOutputVoltage(serial_number)

    return output


KPC_GetMaximumTravel = lib.KPC_GetMaximumTravel
KPC_GetMaximumTravel.restype = c_long
KPC_GetMaximumTravel.argtypes = [POINTER(c_char)]


def get_maximum_travel(serial_number):
    '''
    Gets the maximum travel of the strain gauge.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetMaximumTravel(serial_number)

    return output


KPC_GetNextMessage = lib.KPC_GetNextMessage
KPC_GetNextMessage.restype = c_bool
KPC_GetNextMessage.argtypes = [POINTER(c_char)]


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

    output = KPC_GetNextMessage(serial_number)

    return output


KPC_GetOutputVoltage = lib.KPC_GetOutputVoltage
KPC_GetOutputVoltage.restype = c_short
KPC_GetOutputVoltage.argtypes = [POINTER(c_char)]


def get_output_voltage(serial_number):
    '''
    Gets the actual output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetOutputVoltage(serial_number)

    return output


KPC_GetPosition = lib.KPC_GetPosition
KPC_GetPosition.restype = c_long
KPC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    '''
    Gets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetPosition(serial_number)

    return output


KPC_GetPositionControlMode = lib.KPC_GetPositionControlMode
KPC_GetPositionControlMode.restype = PZ_ControlModeTypes
KPC_GetPositionControlMode.argtypes = [POINTER(c_char)]


def get_position_control_mode(serial_number):
    '''
    Gets the Position Control Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        PZ_ControlModeTypes
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetPositionControlMode(serial_number)

    return output


KPC_GetSoftwareVersion = lib.KPC_GetSoftwareVersion
KPC_GetSoftwareVersion.restype = c_ulong
KPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    output = KPC_GetSoftwareVersion(serial_number)

    return output


KPC_GetStatusBits = lib.KPC_GetStatusBits
KPC_GetStatusBits.restype = c_ulong
KPC_GetStatusBits.argtypes = [POINTER(c_char)]


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

    output = KPC_GetStatusBits(serial_number)

    return output


KPC_GetTriggerConfigParams = lib.KPC_GetTriggerConfigParams
KPC_GetTriggerConfigParams.restype = c_short
KPC_GetTriggerConfigParams.argtypes = [POINTER(c_char)]


def get_trigger_config_params(serial_number):
    '''
    Get the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KPC_TriggerPortMode
        trigger1Polarity: KPC_TriggerPortPolarity
        trigger2Mode: KPC_TriggerPortMode
        trigger2Polarity: KPC_TriggerPortPolarity
        lowerLimit: c_int32
        upperLimit: c_int32
        smoothingSamples: c_int16
        monitorOutput: KPC_MonitorOutputMode
        monitorFilterFrequency: c_int16
        monitorOutputSoftwareValue: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    trigger1Mode = KPC_TriggerPortMode()
    trigger1Polarity = KPC_TriggerPortPolarity()
    trigger2Mode = KPC_TriggerPortMode()
    trigger2Polarity = KPC_TriggerPortPolarity()
    lowerLimit = c_int32()
    upperLimit = c_int32()
    smoothingSamples = c_int16()
    monitorOutput = KPC_MonitorOutputMode()
    monitorFilterFrequency = c_int16()
    monitorOutputSoftwareValue = c_int16()

    output = KPC_GetTriggerConfigParams(serial_number)

    return output


KPC_GetTriggerConfigParamsBlock = lib.KPC_GetTriggerConfigParamsBlock
KPC_GetTriggerConfigParamsBlock.restype = c_short
KPC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char)]


def get_trigger_config_params_block(serial_number):
    '''
    Gets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KPC_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerConfigParams = KPC_TriggerConfig()

    output = KPC_GetTriggerConfigParamsBlock(serial_number)

    return output


KPC_GetVoltageSource = lib.KPC_GetVoltageSource
KPC_GetVoltageSource.restype = PZ_InputSourceFlags
KPC_GetVoltageSource.argtypes = [POINTER(c_char)]


def get_voltage_source(serial_number):
    '''
    Gets the control voltage source.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        PZ_InputSourceFlags
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_GetVoltageSource(serial_number)

    return output


KPC_HasLastMsgTimerOverrun = lib.KPC_HasLastMsgTimerOverrun
KPC_HasLastMsgTimerOverrun.restype = c_bool
KPC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by KPC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_HasLastMsgTimerOverrun(serial_number)

    return output


KPC_Identify = lib.KPC_Identify
KPC_Identify.restype = c_void_p
KPC_Identify.argtypes = [POINTER(c_char)]


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

    output = KPC_Identify(serial_number)

    return output


KPC_LoadNamedSettings = lib.KPC_LoadNamedSettings
KPC_LoadNamedSettings.restype = c_bool
KPC_LoadNamedSettings.argtypes = [POINTER(c_char)]


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

    output = KPC_LoadNamedSettings(serial_number)

    return output


KPC_LoadSettings = lib.KPC_LoadSettings
KPC_LoadSettings.restype = c_bool
KPC_LoadSettings.argtypes = [POINTER(c_char)]


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

    output = KPC_LoadSettings(serial_number)

    return output


KPC_MessageQueueSize = lib.KPC_MessageQueueSize
KPC_MessageQueueSize.restype = c_int
KPC_MessageQueueSize.argtypes = [POINTER(c_char)]


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

    output = KPC_MessageQueueSize(serial_number)

    return output


KPC_Open = lib.KPC_Open
KPC_Open.restype = c_short
KPC_Open.argtypes = [POINTER(c_char)]


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

    output = KPC_Open(serial_number)

    return output


KPC_PersistSettings = lib.KPC_PersistSettings
KPC_PersistSettings.restype = c_bool
KPC_PersistSettings.argtypes = [POINTER(c_char)]


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

    output = KPC_PersistSettings(serial_number)

    return output


KPC_PollingDuration = lib.KPC_PollingDuration
KPC_PollingDuration.restype = c_long
KPC_PollingDuration.argtypes = [POINTER(c_char)]


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

    output = KPC_PollingDuration(serial_number)

    return output


KPC_RegisterMessageCallback = lib.KPC_RegisterMessageCallback
KPC_RegisterMessageCallback.restype = c_void_p
KPC_RegisterMessageCallback.argtypes = [POINTER(c_char)]


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

    output = KPC_RegisterMessageCallback(serial_number)

    return output


KPC_RequestActualPosition = lib.KPC_RequestActualPosition
KPC_RequestActualPosition.restype = c_short
KPC_RequestActualPosition.argtypes = [POINTER(c_char)]


def request_actual_position(serial_number):
    '''
    Requests the position index.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestActualPosition(serial_number)

    return output


KPC_RequestDigitalOutputs = lib.KPC_RequestDigitalOutputs
KPC_RequestDigitalOutputs.restype = c_short
KPC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]


def request_digital_outputs(serial_number):
    '''
    Requests the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestDigitalOutputs(serial_number)

    return output


KPC_RequestFeedbackLoopPIconsts = lib.KPC_RequestFeedbackLoopPIconsts
KPC_RequestFeedbackLoopPIconsts.restype = c_bool
KPC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def request_feedback_loop_p_iconsts(serial_number):
    '''
    Requests that the feedback loop constants be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestFeedbackLoopPIconsts(serial_number)

    return output


KPC_RequestFrontPanelLocked = lib.KPC_RequestFrontPanelLocked
KPC_RequestFrontPanelLocked.restype = c_short
KPC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


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

    output = KPC_RequestFrontPanelLocked(serial_number)

    return output


KPC_RequestHardwareMaxOutputVoltage = lib.KPC_RequestHardwareMaxOutputVoltage
KPC_RequestHardwareMaxOutputVoltage.restype = c_bool
KPC_RequestHardwareMaxOutputVoltage.argtypes = [POINTER(c_char)]


def request_hardware_max_output_voltage(serial_number):
    '''
    Requests the hardware maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestHardwareMaxOutputVoltage(serial_number)

    return output


KPC_RequestIOSettings = lib.KPC_RequestIOSettings
KPC_RequestIOSettings.restype = c_bool
KPC_RequestIOSettings.argtypes = [POINTER(c_char)]


def request_i_o_settings(serial_number):
    '''
    Requests that the IO settings are read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestIOSettings(serial_number)

    return output


KPC_RequestLEDBrightness = lib.KPC_RequestLEDBrightness
KPC_RequestLEDBrightness.restype = c_bool
KPC_RequestLEDBrightness.argtypes = [POINTER(c_char)]


def request_l_e_d_brightness(serial_number):
    '''
    Requests that the LED brightness be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestLEDBrightness(serial_number)

    return output


KPC_RequestMMIParams = lib.KPC_RequestMMIParams
KPC_RequestMMIParams.restype = c_bool
KPC_RequestMMIParams.argtypes = [POINTER(c_char)]


def request_m_m_i_params(serial_number):
    '''
    Request that the MMI Parameters for the KCube Display Interface be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestMMIParams(serial_number)

    return output


KPC_RequestMaxOutputVoltage = lib.KPC_RequestMaxOutputVoltage
KPC_RequestMaxOutputVoltage.restype = c_bool
KPC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]


def request_max_output_voltage(serial_number):
    '''
    Requests the maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestMaxOutputVoltage(serial_number)

    return output


KPC_RequestMaximumTravel = lib.KPC_RequestMaximumTravel
KPC_RequestMaximumTravel.restype = c_short
KPC_RequestMaximumTravel.argtypes = [POINTER(c_char)]


def request_maximum_travel(serial_number):
    '''
    Requests the maximum position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestMaximumTravel(serial_number)

    return output


KPC_RequestOutputVoltage = lib.KPC_RequestOutputVoltage
KPC_RequestOutputVoltage.restype = c_short
KPC_RequestOutputVoltage.argtypes = [POINTER(c_char)]


def request_output_voltage(serial_number):
    '''
    Request output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestOutputVoltage(serial_number)

    return output


KPC_RequestPosition = lib.KPC_RequestPosition
KPC_RequestPosition.restype = c_short
KPC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    '''
    Requests the current output voltage or position depending on current mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestPosition(serial_number)

    return output


KPC_RequestPositionControlMode = lib.KPC_RequestPositionControlMode
KPC_RequestPositionControlMode.restype = c_bool
KPC_RequestPositionControlMode.argtypes = [POINTER(c_char)]


def request_position_control_mode(serial_number):
    '''
    Requests the position control mode from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestPositionControlMode(serial_number)

    return output


KPC_RequestSettings = lib.KPC_RequestSettings
KPC_RequestSettings.restype = c_short
KPC_RequestSettings.argtypes = [POINTER(c_char)]


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

    output = KPC_RequestSettings(serial_number)

    return output


KPC_RequestStatus = lib.KPC_RequestStatus
KPC_RequestStatus.restype = c_short
KPC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    '''
    Requests the status and position from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestStatus(serial_number)

    return output


KPC_RequestStatusBits = lib.KPC_RequestStatusBits
KPC_RequestStatusBits.restype = c_short
KPC_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    output = KPC_RequestStatusBits(serial_number)

    return output


KPC_RequestTriggerConfigParams = lib.KPC_RequestTriggerConfigParams
KPC_RequestTriggerConfigParams.restype = c_short
KPC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    '''
    Request the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestTriggerConfigParams(serial_number)

    return output


KPC_RequestVoltageSource = lib.KPC_RequestVoltageSource
KPC_RequestVoltageSource.restype = c_bool
KPC_RequestVoltageSource.argtypes = [POINTER(c_char)]


def request_voltage_source(serial_number):
    '''
    Requests that the current input voltage source be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_RequestVoltageSource(serial_number)

    return output


KPC_ResetParameters = lib.KPC_ResetParameters
KPC_ResetParameters.restype = c_short
KPC_ResetParameters.argtypes = [POINTER(c_char)]


def reset_parameters(serial_number):
    '''
    Reset parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_ResetParameters(serial_number)

    return output


KPC_SetDigitalOutputs = lib.KPC_SetDigitalOutputs
KPC_SetDigitalOutputs.restype = c_short
KPC_SetDigitalOutputs.argtypes = [POINTER(c_char)]


def set_digital_outputs(serial_number):
    '''
    Sets the digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        outputsBits: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    outputsBits = c_byte()

    output = KPC_SetDigitalOutputs(serial_number)

    return output


KPC_SetFeedbackLoopPIconsts = lib.KPC_SetFeedbackLoopPIconsts
KPC_SetFeedbackLoopPIconsts.restype = c_short
KPC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def set_feedback_loop_p_iconsts(serial_number):
    '''
    Sets the feedback loop constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalTerm: c_short
        integralTerm: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = KPC_SetFeedbackLoopPIconsts(serial_number)

    return output


KPC_SetFeedbackLoopPIconstsBlock = lib.KPC_SetFeedbackLoopPIconstsBlock
KPC_SetFeedbackLoopPIconstsBlock.restype = c_short
KPC_SetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


def set_feedback_loop_p_iconsts_block(serial_number):
    '''
    Sets the feedback loop constants in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        proportionalAndIntegralConstants: PZ_FeedbackLoopConstants

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = KPC_SetFeedbackLoopPIconstsBlock(serial_number)

    return output


KPC_SetFrontPanelLock = lib.KPC_SetFrontPanelLock
KPC_SetFrontPanelLock.restype = c_short
KPC_SetFrontPanelLock.argtypes = [POINTER(c_char)]


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

    output = KPC_SetFrontPanelLock(serial_number)

    return output


KPC_SetHardwareMaxOutputVoltage = lib.KPC_SetHardwareMaxOutputVoltage
KPC_SetHardwareMaxOutputVoltage.restype = c_short
KPC_SetHardwareMaxOutputVoltage.argtypes = [POINTER(c_char)]


def set_hardware_max_output_voltage(serial_number):
    '''
    Sets the hardware maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        hardwareMaxVoltage: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    hardwareMaxVoltage = c_short()

    output = KPC_SetHardwareMaxOutputVoltage(serial_number)

    return output


KPC_SetHubAnalogInput = lib.KPC_SetHubAnalogInput
KPC_SetHubAnalogInput.restype = c_short
KPC_SetHubAnalogInput.argtypes = [POINTER(c_char)]


def set_hub_analog_input(serial_number):
    '''
    Sets the Hub Analog Input.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        hubAnalogInput: KPC_HubAnalogueModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    hubAnalogInput = KPC_HubAnalogueModes()

    output = KPC_SetHubAnalogInput(serial_number)

    return output


KPC_SetIOSettings = lib.KPC_SetIOSettings
KPC_SetIOSettings.restype = c_short
KPC_SetIOSettings.argtypes = [POINTER(c_char)]


def set_i_o_settings(serial_number):
    '''
    Sets the IO settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        ioSettings: KPC_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    ioSettings = KPC_IOSettings()

    output = KPC_SetIOSettings(serial_number)

    return output


KPC_SetLEDBrightness = lib.KPC_SetLEDBrightness
KPC_SetLEDBrightness.restype = c_short
KPC_SetLEDBrightness.argtypes = [POINTER(c_char)]


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

    output = KPC_SetLEDBrightness(serial_number)

    return output


KPC_SetLUTwaveParams = lib.KPC_SetLUTwaveParams
KPC_SetLUTwaveParams.restype = c_short
KPC_SetLUTwaveParams.argtypes = [POINTER(c_char)]


def set_l_u_twave_params(serial_number):
    '''
    Sets the LUT output wave parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        LUTwaveParams: PZ_LUTWaveParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    LUTwaveParams = PZ_LUTWaveParameters()

    output = KPC_SetLUTwaveParams(serial_number)

    return output


KPC_SetLUTwaveSample = lib.KPC_SetLUTwaveSample
KPC_SetLUTwaveSample.restype = c_short
KPC_SetLUTwaveSample.argtypes = [POINTER(c_char)]


def set_l_u_twave_sample(serial_number):
    '''
    Sets a waveform sample.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_short
        value: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    index = c_short()
    value = c_long()

    output = KPC_SetLUTwaveSample(serial_number)

    return output


KPC_SetMMIParams = lib.KPC_SetMMIParams
KPC_SetMMIParams.restype = c_short
KPC_SetMMIParams.argtypes = [POINTER(c_char)]


def set_m_m_i_params(serial_number):
    '''
    Set the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KPZ_WheelMode
        voltageAdjustRate: KPZ_WheelChangeRate
        voltageStep: c_int16
        positionStep: c_int16
        directionSense: KPZ_WheelDirectionSense
        presetVoltage1: c_int16
        presetVoltage2: c_int16
        presetPosition1: c_int16
        presetPosition2: c_int16
        displayIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int16()
    positionStep = c_int16()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int16()
    presetVoltage2 = c_int16()
    presetPosition1 = c_int16()
    presetPosition2 = c_int16()
    displayIntensity = c_int16()

    output = KPC_SetMMIParams(serial_number)

    return output


KPC_SetMMIParamsBlock = lib.KPC_SetMMIParamsBlock
KPC_SetMMIParamsBlock.restype = c_short
KPC_SetMMIParamsBlock.argtypes = [POINTER(c_char)]


def set_m_m_i_params_block(serial_number):
    '''
    Sets the MMI parameters for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mmiParams: KPC_MMIParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mmiParams = KPC_MMIParams()

    output = KPC_SetMMIParamsBlock(serial_number)

    return output


KPC_SetMMIParamsExt = lib.KPC_SetMMIParamsExt
KPC_SetMMIParamsExt.restype = c_short
KPC_SetMMIParamsExt.argtypes = [POINTER(c_char)]


def set_m_m_i_params_ext(serial_number):
    '''
    Set the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KPZ_WheelMode
        voltageAdjustRate: KPZ_WheelChangeRate
        voltageStep: c_int16
        PositionStep: c_int16
        directionSense: KPZ_WheelDirectionSense
        presetVoltage1: c_int16
        presetVoltage2: c_int16
        presetPositiion1: c_int16
        presetPosition2: c_int16
        displayIntensity: c_int16
        displayTimeout: c_int16
        displayDimIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int16()
    PositionStep = c_int16()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int16()
    presetVoltage2 = c_int16()
    presetPositiion1 = c_int16()
    presetPosition2 = c_int16()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = KPC_SetMMIParamsExt(serial_number)

    return output


KPC_SetMaxOutputVoltage = lib.KPC_SetMaxOutputVoltage
KPC_SetMaxOutputVoltage.restype = c_short
KPC_SetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def set_max_output_voltage(serial_number):
    '''
    Sets the maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        maxVoltage: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    maxVoltage = c_short()

    output = KPC_SetMaxOutputVoltage(serial_number)

    return output


KPC_SetOutputVoltage = lib.KPC_SetOutputVoltage
KPC_SetOutputVoltage.restype = c_short
KPC_SetOutputVoltage.argtypes = [POINTER(c_char)]


def set_output_voltage(serial_number):
    '''
    Sets the output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        volts: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    volts = c_short()

    output = KPC_SetOutputVoltage(serial_number)

    return output


KPC_SetPosition = lib.KPC_SetPosition
KPC_SetPosition.restype = c_short
KPC_SetPosition.argtypes = [POINTER(c_char)]


def set_position(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = c_long()

    output = KPC_SetPosition(serial_number)

    return output


KPC_SetPositionControlMode = lib.KPC_SetPositionControlMode
KPC_SetPositionControlMode.restype = c_short
KPC_SetPositionControlMode.argtypes = [POINTER(c_char)]


def set_position_control_mode(serial_number):
    '''
    Sets the Position Control Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: PZ_ControlModeTypes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = PZ_ControlModeTypes()

    output = KPC_SetPositionControlMode(serial_number)

    return output


KPC_SetPositionToTolerance = lib.KPC_SetPositionToTolerance
KPC_SetPositionToTolerance.restype = c_short
KPC_SetPositionToTolerance.argtypes = [POINTER(c_char)]


def set_position_to_tolerance(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: c_long
        tolerance: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = c_long()
    tolerance = c_long()

    output = KPC_SetPositionToTolerance(serial_number)

    return output


KPC_SetTriggerConfigParams = lib.KPC_SetTriggerConfigParams
KPC_SetTriggerConfigParams.restype = c_short
KPC_SetTriggerConfigParams.argtypes = [POINTER(c_char)]


def set_trigger_config_params(serial_number):
    '''
    Set the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KPC_TriggerPortMode
        trigger1Polarity: KPC_TriggerPortPolarity
        trigger2Mode: KPC_TriggerPortMode
        trigger2Polarity: KPC_TriggerPortPolarity
        lowerLimit: c_int32
        upperLimit: c_int32
        smoothingSamples: c_int16
        monitorOutput: KPC_MonitorOutputMode
        monitorFilterFrequency: c_int16
        monitorOutputSoftwareValue: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    trigger1Mode = KPC_TriggerPortMode()
    trigger1Polarity = KPC_TriggerPortPolarity()
    trigger2Mode = KPC_TriggerPortMode()
    trigger2Polarity = KPC_TriggerPortPolarity()
    lowerLimit = c_int32()
    upperLimit = c_int32()
    smoothingSamples = c_int16()
    monitorOutput = KPC_MonitorOutputMode()
    monitorFilterFrequency = c_int16()
    monitorOutputSoftwareValue = c_int16()

    output = KPC_SetTriggerConfigParams(serial_number)

    return output


KPC_SetTriggerConfigParamsBlock = lib.KPC_SetTriggerConfigParamsBlock
KPC_SetTriggerConfigParamsBlock.restype = c_short
KPC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char)]


def set_trigger_config_params_block(serial_number):
    '''
    Sets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KPC_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerConfigParams = KPC_TriggerConfig()

    output = KPC_SetTriggerConfigParamsBlock(serial_number)

    return output


KPC_SetVoltageSource = lib.KPC_SetVoltageSource
KPC_SetVoltageSource.restype = c_short
KPC_SetVoltageSource.argtypes = [POINTER(c_char)]


def set_voltage_source(serial_number):
    '''
    Sets the control voltage source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        source: PZ_InputSourceFlags

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    source = PZ_InputSourceFlags()

    output = KPC_SetVoltageSource(serial_number)

    return output


KPC_SetZero = lib.KPC_SetZero
KPC_SetZero.restype = c_bool
KPC_SetZero.argtypes = [POINTER(c_char)]


def set_zero(serial_number):
    '''
    Set zero reference voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_SetZero(serial_number)

    return output


KPC_StartLUTwave = lib.KPC_StartLUTwave
KPC_StartLUTwave.restype = c_short
KPC_StartLUTwave.argtypes = [POINTER(c_char)]


def start_l_u_twave(serial_number):
    '''
    Starts the LUT waveform output.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_StartLUTwave(serial_number)

    return output


KPC_StartPolling = lib.KPC_StartPolling
KPC_StartPolling.restype = c_bool
KPC_StartPolling.argtypes = [POINTER(c_char)]


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

    output = KPC_StartPolling(serial_number)

    return output


KPC_StopLUTwave = lib.KPC_StopLUTwave
KPC_StopLUTwave.restype = c_short
KPC_StopLUTwave.argtypes = [POINTER(c_char)]


def stop_l_u_twave(serial_number):
    '''
    Stops the LUT waveform output.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = KPC_StopLUTwave(serial_number)

    return output


KPC_StopPolling = lib.KPC_StopPolling
KPC_StopPolling.restype = c_void_p
KPC_StopPolling.argtypes = [POINTER(c_char)]


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

    output = KPC_StopPolling(serial_number)

    return output


KPC_TimeSinceLastMsgReceived = lib.KPC_TimeSinceLastMsgReceived
KPC_TimeSinceLastMsgReceived.restype = c_bool
KPC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


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

    output = KPC_TimeSinceLastMsgReceived(serial_number)

    return output


KPC_WaitForMessage = lib.KPC_WaitForMessage
KPC_WaitForMessage.restype = c_bool
KPC_WaitForMessage.argtypes = [POINTER(c_char)]


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

    output = KPC_WaitForMessage(serial_number)

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



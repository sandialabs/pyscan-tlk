from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_int,
    c_int16,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_ulong,
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    HubAnalogueModes,
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity,
    KPZ_WheelChangeRate,
    KPZ_WheelDirectionSense,
    KPZ_WheelMode,
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
    KPZ_MMIParams,
    KPZ_TriggerConfig,
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation,
    TPZ_IOSettings)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.Piezo.DLL")

PCC_CanDeviceLockFrontPanel = lib.PCC_CanDeviceLockFrontPanel
PCC_CanDeviceLockFrontPanel.restype = c_bool
PCC_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = PCC_CanDeviceLockFrontPanel(serial_number)

    return output


PCC_CheckConnection = lib.PCC_CheckConnection
PCC_CheckConnection.restype = c_bool
PCC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = PCC_CheckConnection(serial_number)

    return output


PCC_ClearMessageQueue = lib.PCC_ClearMessageQueue
PCC_ClearMessageQueue.restype = c_void_p
PCC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = PCC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_Close = lib.PCC_Close
PCC_Close.restype = c_void_p
PCC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = PCC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_Disable = lib.PCC_Disable
PCC_Disable.restype = c_short
PCC_Disable.argtypes = [POINTER(c_char)]


def disable(serial_number):
    # Disable the cube.

    serial_number = POINTER(c_char)

    output = PCC_Disable(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_Disconnect = lib.PCC_Disconnect
PCC_Disconnect.restype = c_short
PCC_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = PCC_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_Enable = lib.PCC_Enable
PCC_Enable.restype = c_short
PCC_Enable.argtypes = [POINTER(c_char)]


def enable(serial_number):
    # Enable cube for computer control.

    serial_number = POINTER(c_char)

    output = PCC_Enable(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_EnableLastMsgTimer = lib.PCC_EnableLastMsgTimer
PCC_EnableLastMsgTimer.restype = c_void_p
PCC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = PCC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


PCC_GetDigitalOutputs = lib.PCC_GetDigitalOutputs
PCC_GetDigitalOutputs.restype = c_byte
PCC_GetDigitalOutputs.argtypes = [POINTER(c_char)]


def get_digital_outputs(serial_number):
    # Gets the digital output bits.

    serial_number = POINTER(c_char)

    output = PCC_GetDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetFeedbackLoopPIconsts = lib.PCC_GetFeedbackLoopPIconsts
PCC_GetFeedbackLoopPIconsts.restype = c_short
PCC_GetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short]


def get_feedback_loop_p_iconsts(serial_number):
    # Gets the feedback loop parameters.

    serial_number = POINTER(c_char)
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = PCC_GetFeedbackLoopPIconsts(serial_number, proportionalTerm, integralTerm)
    if output != 0:
        raise KinesisException(output)


PCC_GetFeedbackLoopPIconstsBlock = lib.PCC_GetFeedbackLoopPIconstsBlock
PCC_GetFeedbackLoopPIconstsBlock.restype = c_short
PCC_GetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char), PZ_FeedbackLoopConstants]


def get_feedback_loop_p_iconsts_block(serial_number):
    # Gets the feedback loop constants in a block.

    serial_number = POINTER(c_char)
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PCC_GetFeedbackLoopPIconstsBlock(serial_number, proportionalAndIntegralConstants)
    if output != 0:
        raise KinesisException(output)


PCC_GetFirmwareVersion = lib.PCC_GetFirmwareVersion
PCC_GetFirmwareVersion.restype = c_ulong
PCC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = PCC_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetFrontPanelLocked = lib.PCC_GetFrontPanelLocked
PCC_GetFrontPanelLocked.restype = c_bool
PCC_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = PCC_GetFrontPanelLocked(serial_number)

    return output


PCC_GetHardwareInfo = lib.PCC_GetHardwareInfo
PCC_GetHardwareInfo.restype = c_short
PCC_GetHardwareInfo.argtypes = [
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

    output = PCC_GetHardwareInfo(
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


PCC_GetHardwareInfoBlock = lib.PCC_GetHardwareInfoBlock
PCC_GetHardwareInfoBlock.restype = c_short
PCC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = PCC_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


PCC_GetHubAnalogInput = lib.PCC_GetHubAnalogInput
PCC_GetHubAnalogInput.restype = HubAnalogueModes
PCC_GetHubAnalogInput.argtypes = [POINTER(c_char)]


def get_hub_analog_input(serial_number):
    # Gets the Hub Analog Input.

    serial_number = POINTER(c_char)

    output = PCC_GetHubAnalogInput(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetIOSettings = lib.PCC_GetIOSettings
PCC_GetIOSettings.restype = TPZ_IOSettings
PCC_GetIOSettings.argtypes = [POINTER(c_char)]


def get_i_o_settings(serial_number):
    # Gets the IO settings.

    serial_number = POINTER(c_char)

    output = PCC_GetIOSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetLEDBrightness = lib.PCC_GetLEDBrightness
PCC_GetLEDBrightness.restype = c_short
PCC_GetLEDBrightness.argtypes = [POINTER(c_char)]


def get_l_e_d_brightness(serial_number):
    # Gets the LED brightness.

    serial_number = POINTER(c_char)

    output = PCC_GetLEDBrightness(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetMMIParams = lib.PCC_GetMMIParams
PCC_GetMMIParams.restype = c_short
PCC_GetMMIParams.argtypes = [
    POINTER(c_char),
    KPZ_WheelMode,
    KPZ_WheelChangeRate,
    c_int32,
    KPZ_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def get_m_m_i_params(serial_number):
    # Get the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int32()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int32()
    presetVoltage2 = c_int32()
    displayIntensity = c_int16()

    output = PCC_GetMMIParams(
        serial_number,
        wheelMode,
        voltageAdjustRate,
        voltageStep,
        directionSense,
        presetVoltage1,
        presetVoltage2,
        displayIntensity)
    if output != 0:
        raise KinesisException(output)


PCC_GetMMIParamsBlock = lib.PCC_GetMMIParamsBlock
PCC_GetMMIParamsBlock.restype = c_short
PCC_GetMMIParamsBlock.argtypes = [POINTER(c_char), KPZ_MMIParams]


def get_m_m_i_params_block(serial_number):
    # Gets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KPZ_MMIParams()

    output = PCC_GetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


PCC_GetMMIParamsExt = lib.PCC_GetMMIParamsExt
PCC_GetMMIParamsExt.restype = c_short
PCC_GetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KPZ_WheelMode,
    KPZ_WheelChangeRate,
    c_int32,
    KPZ_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16,
    c_int16,
    c_int16]


def get_m_m_i_params_ext(serial_number):
    # Get the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int32()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int32()
    presetVoltage2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = PCC_GetMMIParamsExt(
        serial_number,
        wheelMode,
        voltageAdjustRate,
        voltageStep,
        directionSense,
        presetVoltage1,
        presetVoltage2,
        displayIntensity,
        displayTimeout,
        displayDimIntensity)
    if output != 0:
        raise KinesisException(output)


PCC_GetMaxOutputVoltage = lib.PCC_GetMaxOutputVoltage
PCC_GetMaxOutputVoltage.restype = c_short
PCC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def get_max_output_voltage(serial_number):
    # Gets the maximum output voltage.

    serial_number = POINTER(c_char)

    output = PCC_GetMaxOutputVoltage(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetNextMessage = lib.PCC_GetNextMessage
PCC_GetNextMessage.restype = c_bool
PCC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PCC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


PCC_GetOutputVoltage = lib.PCC_GetOutputVoltage
PCC_GetOutputVoltage.restype = c_short
PCC_GetOutputVoltage.argtypes = [POINTER(c_char)]


def get_output_voltage(serial_number):
    # Gets the set Output Voltage.

    serial_number = POINTER(c_char)

    output = PCC_GetOutputVoltage(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetPosition = lib.PCC_GetPosition
PCC_GetPosition.restype = c_long
PCC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Gets the position when in closed loop mode.

    serial_number = POINTER(c_char)

    output = PCC_GetPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetPositionControlMode = lib.PCC_GetPositionControlMode
PCC_GetPositionControlMode.restype = PZ_ControlModeTypes
PCC_GetPositionControlMode.argtypes = [POINTER(c_char)]


def get_position_control_mode(serial_number):
    # Gets the Position Control Mode.

    serial_number = POINTER(c_char)

    output = PCC_GetPositionControlMode(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetSoftwareVersion = lib.PCC_GetSoftwareVersion
PCC_GetSoftwareVersion.restype = c_ulong
PCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = PCC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetStatusBits = lib.PCC_GetStatusBits
PCC_GetStatusBits.restype = c_ulong
PCC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = PCC_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_GetTriggerConfigParams = lib.PCC_GetTriggerConfigParams
PCC_GetTriggerConfigParams.restype = c_short
PCC_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity,
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity]


def get_trigger_config_params(serial_number):
    # Get the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KPZ_TriggerPortMode()
    trigger1Polarity = KPZ_TriggerPortPolarity()
    trigger2Mode = KPZ_TriggerPortMode()
    trigger2Polarity = KPZ_TriggerPortPolarity()

    output = PCC_GetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


PCC_GetTriggerConfigParamsBlock = lib.PCC_GetTriggerConfigParamsBlock
PCC_GetTriggerConfigParamsBlock.restype = c_short
PCC_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPZ_TriggerConfig]


def get_trigger_config_params_block(serial_number):
    # Gets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KPZ_TriggerConfig()

    output = PCC_GetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


PCC_GetVoltageSource = lib.PCC_GetVoltageSource
PCC_GetVoltageSource.restype = PZ_InputSourceFlags
PCC_GetVoltageSource.argtypes = [POINTER(c_char)]


def get_voltage_source(serial_number):
    # Gets the control voltage source.

    serial_number = POINTER(c_char)

    output = PCC_GetVoltageSource(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_HasLastMsgTimerOverrun = lib.PCC_HasLastMsgTimerOverrun
PCC_HasLastMsgTimerOverrun.restype = c_bool
PCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by PCC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = PCC_HasLastMsgTimerOverrun(serial_number)

    return output


PCC_Identify = lib.PCC_Identify
PCC_Identify.restype = c_void_p
PCC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = PCC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_LoadNamedSettings = lib.PCC_LoadNamedSettings
PCC_LoadNamedSettings.restype = c_bool
PCC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = PCC_LoadNamedSettings(serial_number, settingsName)

    return output


PCC_LoadSettings = lib.PCC_LoadSettings
PCC_LoadSettings.restype = c_bool
PCC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = PCC_LoadSettings(serial_number)

    return output


PCC_MessageQueueSize = lib.PCC_MessageQueueSize
PCC_MessageQueueSize.restype = c_int
PCC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = PCC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_Open = lib.PCC_Open
PCC_Open.restype = c_short
PCC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = PCC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_PersistSettings = lib.PCC_PersistSettings
PCC_PersistSettings.restype = c_bool
PCC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # persist the devices current settings.

    serial_number = POINTER(c_char)

    output = PCC_PersistSettings(serial_number)

    return output


PCC_PollingDuration = lib.PCC_PollingDuration
PCC_PollingDuration.restype = c_long
PCC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = PCC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RegisterMessageCallback = lib.PCC_RegisterMessageCallback
PCC_RegisterMessageCallback.restype = c_void_p
PCC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = PCC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


PCC_RequestActualPosition = lib.PCC_RequestActualPosition
PCC_RequestActualPosition.restype = c_short
PCC_RequestActualPosition.argtypes = [POINTER(c_char)]


def request_actual_position(serial_number):
    # Requests the position index.

    serial_number = POINTER(c_char)

    output = PCC_RequestActualPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestDigitalOutputs = lib.PCC_RequestDigitalOutputs
PCC_RequestDigitalOutputs.restype = c_short
PCC_RequestDigitalOutputs.argtypes = [POINTER(c_char)]


def request_digital_outputs(serial_number):
    # Requests the digital output bits.

    serial_number = POINTER(c_char)

    output = PCC_RequestDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestFeedbackLoopPIconsts = lib.PCC_RequestFeedbackLoopPIconsts
PCC_RequestFeedbackLoopPIconsts.restype = c_bool
PCC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def request_feedback_loop_p_iconsts(serial_number):
    # Requests that the feedback loop constants be read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestFeedbackLoopPIconsts(serial_number)

    return output


PCC_RequestFrontPanelLocked = lib.PCC_RequestFrontPanelLocked
PCC_RequestFrontPanelLocked.restype = c_short
PCC_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = PCC_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestIOSettings = lib.PCC_RequestIOSettings
PCC_RequestIOSettings.restype = c_bool
PCC_RequestIOSettings.argtypes = [POINTER(c_char)]


def request_i_o_settings(serial_number):
    # Requests that the IO settings are read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestIOSettings(serial_number)

    return output


PCC_RequestLEDBrightness = lib.PCC_RequestLEDBrightness
PCC_RequestLEDBrightness.restype = c_bool
PCC_RequestLEDBrightness.argtypes = [POINTER(c_char)]


def request_l_e_d_brightness(serial_number):
    # Requests that the LED brightness be read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestLEDBrightness(serial_number)

    return output


PCC_RequestMMIParams = lib.PCC_RequestMMIParams
PCC_RequestMMIParams.restype = c_bool
PCC_RequestMMIParams.argtypes = [POINTER(c_char)]


def request_m_m_i_params(serial_number):
    # Request that the MMI Parameters for the KCube Display Interface be read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestMMIParams(serial_number)

    return output


PCC_RequestMaxOutputVoltage = lib.PCC_RequestMaxOutputVoltage
PCC_RequestMaxOutputVoltage.restype = c_bool
PCC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]


def request_max_output_voltage(serial_number):
    # Requests the maximum output voltage be read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestMaxOutputVoltage(serial_number)

    return output


PCC_RequestOutputVoltage = lib.PCC_RequestOutputVoltage
PCC_RequestOutputVoltage.restype = c_short
PCC_RequestOutputVoltage.argtypes = [POINTER(c_char)]


def request_output_voltage(serial_number):
    # Requests output voltage.

    serial_number = POINTER(c_char)

    output = PCC_RequestOutputVoltage(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestPosition = lib.PCC_RequestPosition
PCC_RequestPosition.restype = c_short
PCC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Requests the current output voltage or position depending on current mode.

    serial_number = POINTER(c_char)

    output = PCC_RequestPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestPositionControlMode = lib.PCC_RequestPositionControlMode
PCC_RequestPositionControlMode.restype = c_short
PCC_RequestPositionControlMode.argtypes = [POINTER(c_char)]


def request_position_control_mode(serial_number):
    # Requests that the Position Control Mode be read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestPositionControlMode(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestSettings = lib.PCC_RequestSettings
PCC_RequestSettings.restype = c_short
PCC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = PCC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestStatus = lib.PCC_RequestStatus
PCC_RequestStatus.restype = c_short
PCC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the status and position from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestStatusBits = lib.PCC_RequestStatusBits
PCC_RequestStatusBits.restype = c_short
PCC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = PCC_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_RequestTriggerConfigParams = lib.PCC_RequestTriggerConfigParams
PCC_RequestTriggerConfigParams.restype = c_bool
PCC_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    # Requests that the trigger config parameters are read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestTriggerConfigParams(serial_number)

    return output


PCC_RequestVoltageSource = lib.PCC_RequestVoltageSource
PCC_RequestVoltageSource.restype = c_bool
PCC_RequestVoltageSource.argtypes = [POINTER(c_char)]


def request_voltage_source(serial_number):
    # Requests that the current input voltage source be read from the device.

    serial_number = POINTER(c_char)

    output = PCC_RequestVoltageSource(serial_number)

    return output


PCC_SetDigitalOutputs = lib.PCC_SetDigitalOutputs
PCC_SetDigitalOutputs.restype = c_short
PCC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_byte]


def set_digital_outputs(serial_number):
    # Sets the digital output bits.

    serial_number = POINTER(c_char)
    outputsBits = c_byte()

    output = PCC_SetDigitalOutputs(serial_number, outputsBits)
    if output != 0:
        raise KinesisException(output)


PCC_SetFeedbackLoopPIconsts = lib.PCC_SetFeedbackLoopPIconsts
PCC_SetFeedbackLoopPIconsts.restype = c_short
PCC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short]


def set_feedback_loop_p_iconsts(serial_number):
    # Sets the feedback loop constants.

    serial_number = POINTER(c_char)
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = PCC_SetFeedbackLoopPIconsts(serial_number, proportionalTerm, integralTerm)
    if output != 0:
        raise KinesisException(output)


PCC_SetFeedbackLoopPIconstsBlock = lib.PCC_SetFeedbackLoopPIconstsBlock
PCC_SetFeedbackLoopPIconstsBlock.restype = c_short
PCC_SetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char), PZ_FeedbackLoopConstants]


def set_feedback_loop_p_iconsts_block(serial_number):
    # Sets the feedback loop constants in a block.

    serial_number = POINTER(c_char)
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PCC_SetFeedbackLoopPIconstsBlock(serial_number, proportionalAndIntegralConstants)
    if output != 0:
        raise KinesisException(output)


PCC_SetFrontPanelLock = lib.PCC_SetFrontPanelLock
PCC_SetFrontPanelLock.restype = c_short
PCC_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = PCC_SetFrontPanelLock(serial_number, locked)
    if output != 0:
        raise KinesisException(output)


PCC_SetHubAnalogInput = lib.PCC_SetHubAnalogInput
PCC_SetHubAnalogInput.restype = c_short
PCC_SetHubAnalogInput.argtypes = [POINTER(c_char), HubAnalogueModes]


def set_hub_analog_input(serial_number):
    # Sets the Hub Analog Input.

    serial_number = POINTER(c_char)
    hubAnalogInput = HubAnalogueModes()

    output = PCC_SetHubAnalogInput(serial_number, hubAnalogInput)
    if output != 0:
        raise KinesisException(output)


PCC_SetIOSettings = lib.PCC_SetIOSettings
PCC_SetIOSettings.restype = c_short
PCC_SetIOSettings.argtypes = [POINTER(c_char), TPZ_IOSettings]


def set_i_o_settings(serial_number):
    # Sets the IO settings.

    serial_number = POINTER(c_char)
    ioSettings = TPZ_IOSettings()

    output = PCC_SetIOSettings(serial_number, ioSettings)
    if output != 0:
        raise KinesisException(output)


PCC_SetLEDBrightness = lib.PCC_SetLEDBrightness
PCC_SetLEDBrightness.restype = c_short
PCC_SetLEDBrightness.argtypes = [POINTER(c_char), c_short]


def set_l_e_d_brightness(serial_number):
    # Sets the LED brightness.

    serial_number = POINTER(c_char)
    brightness = c_short()

    output = PCC_SetLEDBrightness(serial_number, brightness)
    if output != 0:
        raise KinesisException(output)


PCC_SetLUTwaveParams = lib.PCC_SetLUTwaveParams
PCC_SetLUTwaveParams.restype = c_short
PCC_SetLUTwaveParams.argtypes = [POINTER(c_char), PZ_LUTWaveParameters]


def set_l_u_twave_params(serial_number):
    # Sets the LUT output wave parameters.

    serial_number = POINTER(c_char)
    LUTwaveParams = PZ_LUTWaveParameters()

    output = PCC_SetLUTwaveParams(serial_number, LUTwaveParams)
    if output != 0:
        raise KinesisException(output)


PCC_SetLUTwaveSample = lib.PCC_SetLUTwaveSample
PCC_SetLUTwaveSample.restype = c_short
PCC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_long]


def set_l_u_twave_sample(serial_number):
    # Sets a waveform sample.

    serial_number = POINTER(c_char)
    index = c_short()
    value = c_long()

    output = PCC_SetLUTwaveSample(serial_number, index, value)
    if output != 0:
        raise KinesisException(output)


PCC_SetMMIParams = lib.PCC_SetMMIParams
PCC_SetMMIParams.restype = c_short
PCC_SetMMIParams.argtypes = [
    POINTER(c_char),
    KPZ_WheelMode,
    KPZ_WheelChangeRate,
    c_int32,
    KPZ_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16]


def set_m_m_i_params(serial_number):
    # Set the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int32()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int32()
    presetVoltage2 = c_int32()
    displayIntensity = c_int16()

    output = PCC_SetMMIParams(
        serial_number,
        wheelMode,
        voltageAdjustRate,
        voltageStep,
        directionSense,
        presetVoltage1,
        presetVoltage2,
        displayIntensity)
    if output != 0:
        raise KinesisException(output)


PCC_SetMMIParamsBlock = lib.PCC_SetMMIParamsBlock
PCC_SetMMIParamsBlock.restype = c_short
PCC_SetMMIParamsBlock.argtypes = [POINTER(c_char), KPZ_MMIParams]


def set_m_m_i_params_block(serial_number):
    # Sets the MMI parameters for the device.

    serial_number = POINTER(c_char)
    mmiParams = KPZ_MMIParams()

    output = PCC_SetMMIParamsBlock(serial_number, mmiParams)
    if output != 0:
        raise KinesisException(output)


PCC_SetMMIParamsExt = lib.PCC_SetMMIParamsExt
PCC_SetMMIParamsExt.restype = c_short
PCC_SetMMIParamsExt.argtypes = [
    POINTER(c_char),
    KPZ_WheelMode,
    KPZ_WheelChangeRate,
    c_int32,
    KPZ_WheelDirectionSense,
    c_int32,
    c_int32,
    c_int16,
    c_int16,
    c_int16]


def set_m_m_i_params_ext(serial_number):
    # Set the MMI Parameters for the KCube Display Interface.

    serial_number = POINTER(c_char)
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int32()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int32()
    presetVoltage2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = PCC_SetMMIParamsExt(
        serial_number,
        wheelMode,
        voltageAdjustRate,
        voltageStep,
        directionSense,
        presetVoltage1,
        presetVoltage2,
        displayIntensity,
        displayTimeout,
        displayDimIntensity)
    if output != 0:
        raise KinesisException(output)


PCC_SetMaxOutputVoltage = lib.PCC_SetMaxOutputVoltage
PCC_SetMaxOutputVoltage.restype = c_short
PCC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]


def set_max_output_voltage(serial_number):
    # Sets the maximum output voltage.

    serial_number = POINTER(c_char)
    maxVoltage = c_short()

    output = PCC_SetMaxOutputVoltage(serial_number, maxVoltage)
    if output != 0:
        raise KinesisException(output)


PCC_SetOutputVoltage = lib.PCC_SetOutputVoltage
PCC_SetOutputVoltage.restype = c_short
PCC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]


def set_output_voltage(serial_number):
    # Sets the output voltage.

    serial_number = POINTER(c_char)
    volts = c_short()

    output = PCC_SetOutputVoltage(serial_number, volts)
    if output != 0:
        raise KinesisException(output)


PCC_SetPosition = lib.PCC_SetPosition
PCC_SetPosition.restype = c_short
PCC_SetPosition.argtypes = [POINTER(c_char), c_long]


def set_position(serial_number):
    # Sets the position when in closed loop mode.

    serial_number = POINTER(c_char)
    position = c_long()

    output = PCC_SetPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


PCC_SetPositionControlMode = lib.PCC_SetPositionControlMode
PCC_SetPositionControlMode.restype = c_short
PCC_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]


def set_position_control_mode(serial_number):
    # Sets the Position Control Mode.

    serial_number = POINTER(c_char)
    mode = PZ_ControlModeTypes()

    output = PCC_SetPositionControlMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


PCC_SetPositionToTolerance = lib.PCC_SetPositionToTolerance
PCC_SetPositionToTolerance.restype = c_short
PCC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_long, c_long]


def set_position_to_tolerance(serial_number):
    # Sets the position when in closed loop mode.

    serial_number = POINTER(c_char)
    position = c_long()
    tolerance = c_long()

    output = PCC_SetPositionToTolerance(serial_number, position, tolerance)
    if output != 0:
        raise KinesisException(output)


PCC_SetTriggerConfigParams = lib.PCC_SetTriggerConfigParams
PCC_SetTriggerConfigParams.restype = c_short
PCC_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity,
    KPZ_TriggerPortMode,
    KPZ_TriggerPortPolarity]


def set_trigger_config_params(serial_number):
    # Set the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KPZ_TriggerPortMode()
    trigger1Polarity = KPZ_TriggerPortPolarity()
    trigger2Mode = KPZ_TriggerPortMode()
    trigger2Polarity = KPZ_TriggerPortPolarity()

    output = PCC_SetTriggerConfigParams(serial_number, trigger1Mode, trigger1Polarity, trigger2Mode, trigger2Polarity)
    if output != 0:
        raise KinesisException(output)


PCC_SetTriggerConfigParamsBlock = lib.PCC_SetTriggerConfigParamsBlock
PCC_SetTriggerConfigParamsBlock.restype = c_short
PCC_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KPZ_TriggerConfig]


def set_trigger_config_params_block(serial_number):
    # Sets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KPZ_TriggerConfig()

    output = PCC_SetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


PCC_SetVoltageSource = lib.PCC_SetVoltageSource
PCC_SetVoltageSource.restype = c_short
PCC_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]


def set_voltage_source(serial_number):
    # Sets the control voltage source.

    serial_number = POINTER(c_char)
    source = PZ_InputSourceFlags()

    output = PCC_SetVoltageSource(serial_number, source)
    if output != 0:
        raise KinesisException(output)


PCC_SetZero = lib.PCC_SetZero
PCC_SetZero.restype = c_bool
PCC_SetZero.argtypes = [POINTER(c_char)]


def set_zero(serial_number):
    # Set zero reference voltage.

    serial_number = POINTER(c_char)

    output = PCC_SetZero(serial_number)

    return output


PCC_StartLUTwave = lib.PCC_StartLUTwave
PCC_StartLUTwave.restype = c_short
PCC_StartLUTwave.argtypes = [POINTER(c_char)]


def start_l_u_twave(serial_number):
    # Starts the LUT waveform output.

    serial_number = POINTER(c_char)

    output = PCC_StartLUTwave(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_StartPolling = lib.PCC_StartPolling
PCC_StartPolling.restype = c_bool
PCC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = PCC_StartPolling(serial_number, milliseconds)

    return output


PCC_StopLUTwave = lib.PCC_StopLUTwave
PCC_StopLUTwave.restype = c_short
PCC_StopLUTwave.argtypes = [POINTER(c_char)]


def stop_l_u_twave(serial_number):
    # Stops the LUT waveform output.

    serial_number = POINTER(c_char)

    output = PCC_StopLUTwave(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_StopPolling = lib.PCC_StopPolling
PCC_StopPolling.restype = c_void_p
PCC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = PCC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


PCC_TimeSinceLastMsgReceived = lib.PCC_TimeSinceLastMsgReceived
PCC_TimeSinceLastMsgReceived.restype = c_bool
PCC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = PCC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


PCC_WaitForMessage = lib.PCC_WaitForMessage
PCC_WaitForMessage.restype = c_bool
PCC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PCC_WaitForMessage(serial_number, messageType, messageID, messageData)

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

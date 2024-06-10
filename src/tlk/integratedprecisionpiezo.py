from ctypes import (POINTER, c_bool, c_byte, c_char, c_int, c_int16, c_int32, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    KPZ_WheelChangeRate,
    KPZ_WheelDirectionSense,
    KPZ_WheelMode,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
    KSG_TriggerConfig,
    PPC_IOSettings,
    PPC_PIDConsts,
    PPC_PIDCriteria,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.IntegratedPrecisionPiezo.DLL")

IPP_CanDeviceLockFrontPanel = lib.IPP_CanDeviceLockFrontPanel
IPP_CanDeviceLockFrontPanel.restype = c_bool
IPP_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


def can_device_lock_front_panel(serial_number):
    # Determine if the device front panel can be locked.

    serial_number = POINTER(c_char)

    output = IPP_CanDeviceLockFrontPanel(serial_number)

    return output


IPP_CheckConnection = lib.IPP_CheckConnection
IPP_CheckConnection.restype = c_bool
IPP_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = IPP_CheckConnection(serial_number)

    return output


IPP_ClearMessageQueue = lib.IPP_ClearMessageQueue
IPP_ClearMessageQueue.restype = c_short
IPP_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = IPP_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_Close = lib.IPP_Close
IPP_Close.restype = c_void_p
IPP_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = IPP_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_DisableChannel = lib.IPP_DisableChannel
IPP_DisableChannel.restype = c_short
IPP_DisableChannel.argtypes = [POINTER(c_char)]


def disable_channel(serial_number):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)

    output = IPP_DisableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_Disconnect = lib.IPP_Disconnect
IPP_Disconnect.restype = c_short
IPP_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = IPP_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_EnableChannel = lib.IPP_EnableChannel
IPP_EnableChannel.restype = c_short
IPP_EnableChannel.argtypes = [POINTER(c_char)]


def enable_channel(serial_number):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)

    output = IPP_EnableChannel(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetFirmwareVersion = lib.IPP_GetFirmwareVersion
IPP_GetFirmwareVersion.restype = c_ulong
IPP_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = IPP_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetFrontPanelLocked = lib.IPP_GetFrontPanelLocked
IPP_GetFrontPanelLocked.restype = c_bool
IPP_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


def get_front_panel_locked(serial_number):
    # Query if the device front panel locked.

    serial_number = POINTER(c_char)

    output = IPP_GetFrontPanelLocked(serial_number)

    return output


IPP_GetHardwareInfo = lib.IPP_GetHardwareInfo
IPP_GetHardwareInfo.restype = c_short
IPP_GetHardwareInfo.argtypes = [
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

    output = IPP_GetHardwareInfo(
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


IPP_GetHardwareInfoBlock = lib.IPP_GetHardwareInfoBlock
IPP_GetHardwareInfoBlock.restype = c_short
IPP_GetHardwareInfoBlock.argtypes = [POINTER(c_char), TLI_HardwareInformation]


def get_hardware_info_block(serial_number):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    hardwareInfo = TLI_HardwareInformation()

    output = IPP_GetHardwareInfoBlock(serial_number, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


IPP_GetIOSettings = lib.IPP_GetIOSettings
IPP_GetIOSettings.restype = c_short
IPP_GetIOSettings.argtypes = [POINTER(c_char), PPC_IOSettings]


def get_i_o_settings(serial_number):
    # Gets the PPC IO Settings.

    serial_number = POINTER(c_char)
    ioSettings = PPC_IOSettings()

    output = IPP_GetIOSettings(serial_number, ioSettings)
    if output != 0:
        raise KinesisException(output)


IPP_GetMMIParams = lib.IPP_GetMMIParams
IPP_GetMMIParams.restype = c_short
IPP_GetMMIParams.argtypes = [
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


def get_m_m_i_params(serial_number):
    # Get the MMI Parameters for the Integrated Precision Piezo.

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

    output = IPP_GetMMIParams(
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


IPP_GetMaxOutputVoltage = lib.IPP_GetMaxOutputVoltage
IPP_GetMaxOutputVoltage.restype = c_short
IPP_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def get_max_output_voltage(serial_number):
    # Gets the maximum output voltage (140V) in units of 1 tenth of a volt

    serial_number = POINTER(c_char)

    output = IPP_GetMaxOutputVoltage(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetMinOutputVoltage = lib.IPP_GetMinOutputVoltage
IPP_GetMinOutputVoltage.restype = c_short
IPP_GetMinOutputVoltage.argtypes = [POINTER(c_char)]


def get_min_output_voltage(serial_number):
    # Gets the minimum output voltage (-10V) in units of 1 tenth of a volt.

    serial_number = POINTER(c_char)

    output = IPP_GetMinOutputVoltage(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetNextMessage = lib.IPP_GetNextMessage
IPP_GetNextMessage.restype = c_bool
IPP_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = IPP_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


IPP_GetOutputVoltage = lib.IPP_GetOutputVoltage
IPP_GetOutputVoltage.restype = c_short
IPP_GetOutputVoltage.argtypes = [POINTER(c_char)]


def get_output_voltage(serial_number):
    # Gets the set Output Voltage.

    serial_number = POINTER(c_char)

    output = IPP_GetOutputVoltage(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetPIDConsts = lib.IPP_GetPIDConsts
IPP_GetPIDConsts.restype = c_short
IPP_GetPIDConsts.argtypes = [POINTER(c_char), c_byte, PPC_PIDConsts]


def get_p_i_d_consts(serial_number):
    # Gets the PPC PID Constants.

    serial_number = POINTER(c_char)
    index = c_byte()
    pidConsts = PPC_PIDConsts()

    output = IPP_GetPIDConsts(serial_number, index, pidConsts)
    if output != 0:
        raise KinesisException(output)


IPP_GetPIDCriteria = lib.IPP_GetPIDCriteria
IPP_GetPIDCriteria.restype = c_short
IPP_GetPIDCriteria.argtypes = [POINTER(c_char), c_byte, PPC_PIDCriteria]


def get_p_i_d_criteria(serial_number):
    # Gets the PID Criteria.

    serial_number = POINTER(c_char)
    criteriaID = c_byte()
    pidCriteria = PPC_PIDCriteria()

    output = IPP_GetPIDCriteria(serial_number, criteriaID, pidCriteria)
    if output != 0:
        raise KinesisException(output)


IPP_GetPosition = lib.IPP_GetPosition
IPP_GetPosition.restype = c_short
IPP_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    # Gets the current position Please note this is non linear

    serial_number = POINTER(c_char)

    output = IPP_GetPosition(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetPositionControlMode = lib.IPP_GetPositionControlMode
IPP_GetPositionControlMode.restype = PZ_ControlModeTypes
IPP_GetPositionControlMode.argtypes = [POINTER(c_char)]


def get_position_control_mode(serial_number):
    # Gets the Position Control Mode.

    serial_number = POINTER(c_char)

    output = IPP_GetPositionControlMode(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetSoftwareVersion = lib.IPP_GetSoftwareVersion
IPP_GetSoftwareVersion.restype = c_ulong
IPP_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = IPP_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetStatusBits = lib.IPP_GetStatusBits
IPP_GetStatusBits.restype = c_ulong
IPP_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)

    output = IPP_GetStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_GetTriggerConfigParams = lib.IPP_GetTriggerConfigParams
IPP_GetTriggerConfigParams.restype = c_short
IPP_GetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    c_int32,
    c_int32,
    c_int16]


def get_trigger_config_params(serial_number):
    # Get the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KSG_TriggerPortMode()
    trigger1Polarity = KSG_TriggerPortPolarity()
    trigger2Mode = KSG_TriggerPortMode()
    trigger2Polarity = KSG_TriggerPortPolarity()
    lowerLimit = c_int32()
    upperLimit = c_int32()
    smoothingSamples = c_int16()

    output = IPP_GetTriggerConfigParams(
        serial_number,
        trigger1Mode,
        trigger1Polarity,
        trigger2Mode,
        trigger2Polarity,
        lowerLimit,
        upperLimit,
        smoothingSamples)
    if output != 0:
        raise KinesisException(output)


IPP_GetTriggerConfigParamsBlock = lib.IPP_GetTriggerConfigParamsBlock
IPP_GetTriggerConfigParamsBlock.restype = c_short
IPP_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSG_TriggerConfig]


def get_trigger_config_params_block(serial_number):
    # Gets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KSG_TriggerConfig()

    output = IPP_GetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


IPP_GetVoltageSource = lib.IPP_GetVoltageSource
IPP_GetVoltageSource.restype = PZ_InputSourceFlags
IPP_GetVoltageSource.argtypes = [POINTER(c_char)]


def get_voltage_source(serial_number):
    # Gets the control voltage source.

    serial_number = POINTER(c_char)

    output = IPP_GetVoltageSource(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_Identify = lib.IPP_Identify
IPP_Identify.restype = c_void_p
IPP_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = IPP_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_LoadNamedSettings = lib.IPP_LoadNamedSettings
IPP_LoadNamedSettings.restype = c_bool
IPP_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = IPP_LoadNamedSettings(serial_number, settingsName)

    return output


IPP_LoadSettings = lib.IPP_LoadSettings
IPP_LoadSettings.restype = c_bool
IPP_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = IPP_LoadSettings(serial_number)

    return output


IPP_MessageQueueSize = lib.IPP_MessageQueueSize
IPP_MessageQueueSize.restype = c_int
IPP_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = IPP_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_Open = lib.IPP_Open
IPP_Open.restype = c_short
IPP_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = IPP_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_PersistSettings = lib.IPP_PersistSettings
IPP_PersistSettings.restype = c_bool
IPP_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # Persist device settings to device.

    serial_number = POINTER(c_char)

    output = IPP_PersistSettings(serial_number)

    return output


IPP_PollingDuration = lib.IPP_PollingDuration
IPP_PollingDuration.restype = c_long
IPP_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = IPP_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_RegisterMessageCallback = lib.IPP_RegisterMessageCallback
IPP_RegisterMessageCallback.restype = c_short
IPP_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = IPP_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


IPP_RequestFrontPanelLocked = lib.IPP_RequestFrontPanelLocked
IPP_RequestFrontPanelLocked.restype = c_short
IPP_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


def request_front_panel_locked(serial_number):
    # Ask the device if its front panel is locked.

    serial_number = POINTER(c_char)

    output = IPP_RequestFrontPanelLocked(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_RequestIOSettings = lib.IPP_RequestIOSettings
IPP_RequestIOSettings.restype = c_bool
IPP_RequestIOSettings.argtypes = [POINTER(c_char)]


def request_i_o_settings(serial_number):
    # Requests the curent PPC IO Setting.

    serial_number = POINTER(c_char)

    output = IPP_RequestIOSettings(serial_number)

    return output


IPP_RequestMMIParams = lib.IPP_RequestMMIParams
IPP_RequestMMIParams.restype = c_bool
IPP_RequestMMIParams.argtypes = [POINTER(c_char)]


def request_m_m_i_params(serial_number):
    # Request that the MMI Parameters for the Integrated Precision Piezo be read from the device.

    serial_number = POINTER(c_char)

    output = IPP_RequestMMIParams(serial_number)

    return output


IPP_RequestOutputVoltage = lib.IPP_RequestOutputVoltage
IPP_RequestOutputVoltage.restype = c_bool
IPP_RequestOutputVoltage.argtypes = [POINTER(c_char)]


def request_output_voltage(serial_number):
    # Requests the maximum output voltage be read from the device.

    serial_number = POINTER(c_char)

    output = IPP_RequestOutputVoltage(serial_number)

    return output


IPP_RequestPIDConsts = lib.IPP_RequestPIDConsts
IPP_RequestPIDConsts.restype = c_short
IPP_RequestPIDConsts.argtypes = [POINTER(c_char), c_byte]


def request_p_i_d_consts(serial_number):
    # Requests the PID Constants.

    serial_number = POINTER(c_char)
    index = c_byte()

    output = IPP_RequestPIDConsts(serial_number, index)
    if output != 0:
        raise KinesisException(output)


IPP_RequestPIDCriteria = lib.IPP_RequestPIDCriteria
IPP_RequestPIDCriteria.restype = c_short
IPP_RequestPIDCriteria.argtypes = [POINTER(c_char), c_byte]


def request_p_i_d_criteria(serial_number):
    # Requests the PID Criteria.

    serial_number = POINTER(c_char)
    criteriaID = c_byte()

    output = IPP_RequestPIDCriteria(serial_number, criteriaID)
    if output != 0:
        raise KinesisException(output)


IPP_RequestPosition = lib.IPP_RequestPosition
IPP_RequestPosition.restype = c_bool
IPP_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    # Gets the current Closed Loop position.

    serial_number = POINTER(c_char)

    output = IPP_RequestPosition(serial_number)

    return output


IPP_RequestPositionControlMode = lib.IPP_RequestPositionControlMode
IPP_RequestPositionControlMode.restype = c_bool
IPP_RequestPositionControlMode.argtypes = [POINTER(c_char)]


def request_position_control_mode(serial_number):
    # Requests that the Position Control Mode be read from the device.

    serial_number = POINTER(c_char)

    output = IPP_RequestPositionControlMode(serial_number)

    return output


IPP_RequestSettings = lib.IPP_RequestSettings
IPP_RequestSettings.restype = c_short
IPP_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = IPP_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_RequestStatus = lib.IPP_RequestStatus
IPP_RequestStatus.restype = c_short
IPP_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Requests the status bits and position.

    serial_number = POINTER(c_char)

    output = IPP_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_RequestStatusBits = lib.IPP_RequestStatusBits
IPP_RequestStatusBits.restype = c_short
IPP_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)

    output = IPP_RequestStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_RequestTriggerConfigParams = lib.IPP_RequestTriggerConfigParams
IPP_RequestTriggerConfigParams.restype = c_short
IPP_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    # Requests the trigger config parameters

    serial_number = POINTER(c_char)

    output = IPP_RequestTriggerConfigParams(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_RequestVoltageSource = lib.IPP_RequestVoltageSource
IPP_RequestVoltageSource.restype = c_bool
IPP_RequestVoltageSource.argtypes = [POINTER(c_char)]


def request_voltage_source(serial_number):
    # Requests that the current input voltage source be read from the device.

    serial_number = POINTER(c_char)

    output = IPP_RequestVoltageSource(serial_number)

    return output


IPP_ResetParameters = lib.IPP_ResetParameters
IPP_ResetParameters.restype = c_short
IPP_ResetParameters.argtypes = [POINTER(c_char)]


def reset_parameters(serial_number):
    # Sets the voltage output to zero and defines the ensuing actuator position az zero.

    serial_number = POINTER(c_char)

    output = IPP_ResetParameters(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_SetFrontPanelLock = lib.IPP_SetFrontPanelLock
IPP_SetFrontPanelLock.restype = c_short
IPP_SetFrontPanelLock.argtypes = [POINTER(c_char), c_bool]


def set_front_panel_lock(serial_number):
    # Sets the device front panel lock state.

    serial_number = POINTER(c_char)
    locked = c_bool()

    output = IPP_SetFrontPanelLock(serial_number, locked)
    if output != 0:
        raise KinesisException(output)


IPP_SetIOSettings = lib.IPP_SetIOSettings
IPP_SetIOSettings.restype = c_short
IPP_SetIOSettings.argtypes = [POINTER(c_char), PPC_IOSettings]


def set_i_o_settings(serial_number):
    # Sets the PPC IO Setting.

    serial_number = POINTER(c_char)
    ioSettings = PPC_IOSettings()

    output = IPP_SetIOSettings(serial_number, ioSettings)
    if output != 0:
        raise KinesisException(output)


IPP_SetMMIParams = lib.IPP_SetMMIParams
IPP_SetMMIParams.restype = c_short
IPP_SetMMIParams.argtypes = [
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


def set_m_m_i_params(serial_number):
    # Set the MMI Parameters for the Integrated PrecisionPiezo.

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

    output = IPP_SetMMIParams(
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


IPP_SetOutputVoltage = lib.IPP_SetOutputVoltage
IPP_SetOutputVoltage.restype = c_short
IPP_SetOutputVoltage.argtypes = [POINTER(c_char), c_short]


def set_output_voltage(serial_number):
    # Sets the output voltage.

    serial_number = POINTER(c_char)
    volts = c_short()

    output = IPP_SetOutputVoltage(serial_number, volts)
    if output != 0:
        raise KinesisException(output)


IPP_SetPIDConsts = lib.IPP_SetPIDConsts
IPP_SetPIDConsts.restype = c_short
IPP_SetPIDConsts.argtypes = [POINTER(c_char), PPC_PIDConsts]


def set_p_i_d_consts(serial_number):
    # Sets the PPC PID Constants.

    serial_number = POINTER(c_char)
    pidConsts = PPC_PIDConsts()

    output = IPP_SetPIDConsts(serial_number, pidConsts)
    if output != 0:
        raise KinesisException(output)


IPP_SetPIDCriteria = lib.IPP_SetPIDCriteria
IPP_SetPIDCriteria.restype = c_short
IPP_SetPIDCriteria.argtypes = [POINTER(c_char), PPC_PIDCriteria]


def set_p_i_d_criteria(serial_number):
    # Sets the PID Criteria.

    serial_number = POINTER(c_char)
    pidCriteria = PPC_PIDCriteria()

    output = IPP_SetPIDCriteria(serial_number, pidCriteria)
    if output != 0:
        raise KinesisException(output)


IPP_SetPosition = lib.IPP_SetPosition
IPP_SetPosition.restype = c_short
IPP_SetPosition.argtypes = [POINTER(c_char), c_short]


def set_position(serial_number):
    # Sets the position when in closed loop mode.

    serial_number = POINTER(c_char)
    position = c_short()

    output = IPP_SetPosition(serial_number, position)
    if output != 0:
        raise KinesisException(output)


IPP_SetPositionControlMode = lib.IPP_SetPositionControlMode
IPP_SetPositionControlMode.restype = c_short
IPP_SetPositionControlMode.argtypes = [POINTER(c_char), PZ_ControlModeTypes]


def set_position_control_mode(serial_number):
    # Sets the Position Control Mode.

    serial_number = POINTER(c_char)
    mode = PZ_ControlModeTypes()

    output = IPP_SetPositionControlMode(serial_number, mode)
    if output != 0:
        raise KinesisException(output)


IPP_SetTriggerConfigParams = lib.IPP_SetTriggerConfigParams
IPP_SetTriggerConfigParams.restype = c_short
IPP_SetTriggerConfigParams.argtypes = [
    POINTER(c_char),
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    KSG_TriggerPortMode,
    KSG_TriggerPortPolarity,
    c_int32,
    c_int32,
    c_int16]


def set_trigger_config_params(serial_number):
    # Set the Trigger Configuration Parameters.

    serial_number = POINTER(c_char)
    trigger1Mode = KSG_TriggerPortMode()
    trigger1Polarity = KSG_TriggerPortPolarity()
    trigger2Mode = KSG_TriggerPortMode()
    trigger2Polarity = KSG_TriggerPortPolarity()
    lowerLimit = c_int32()
    upperLimit = c_int32()
    smoothingSamples = c_int16()

    output = IPP_SetTriggerConfigParams(
        serial_number,
        trigger1Mode,
        trigger1Polarity,
        trigger2Mode,
        trigger2Polarity,
        lowerLimit,
        upperLimit,
        smoothingSamples)
    if output != 0:
        raise KinesisException(output)


IPP_SetTriggerConfigParamsBlock = lib.IPP_SetTriggerConfigParamsBlock
IPP_SetTriggerConfigParamsBlock.restype = c_short
IPP_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char), KSG_TriggerConfig]


def set_trigger_config_params_block(serial_number):
    # Sets the trigger configuration parameters block.

    serial_number = POINTER(c_char)
    triggerConfigParams = KSG_TriggerConfig()

    output = IPP_SetTriggerConfigParamsBlock(serial_number, triggerConfigParams)
    if output != 0:
        raise KinesisException(output)


IPP_SetVoltageSource = lib.IPP_SetVoltageSource
IPP_SetVoltageSource.restype = c_short
IPP_SetVoltageSource.argtypes = [POINTER(c_char), PZ_InputSourceFlags]


def set_voltage_source(serial_number):
    # Sets the control voltage source.

    serial_number = POINTER(c_char)
    source = PZ_InputSourceFlags()

    output = IPP_SetVoltageSource(serial_number, source)
    if output != 0:
        raise KinesisException(output)


IPP_SetZero = lib.IPP_SetZero
IPP_SetZero.restype = c_short
IPP_SetZero.argtypes = [POINTER(c_char)]


def set_zero(serial_number):
    # Performs a Set Zero operation.

    serial_number = POINTER(c_char)

    output = IPP_SetZero(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_StartPolling = lib.IPP_StartPolling
IPP_StartPolling.restype = c_bool
IPP_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = IPP_StartPolling(serial_number, milliseconds)

    return output


IPP_StopPolling = lib.IPP_StopPolling
IPP_StopPolling.restype = c_void_p
IPP_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = IPP_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


IPP_WaitForMessage = lib.IPP_WaitForMessage
IPP_WaitForMessage.restype = c_bool
IPP_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = IPP_WaitForMessage(serial_number, messageType, messageID, messageData)

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

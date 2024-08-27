from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_int,
    c_int16,
    c_int32,
    c_long,
    c_short,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
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

c_short_pointer = type(pointer(c_short()))
c_ulong_pointer = type(pointer(c_ulong()))
c_long_pointer = type(pointer(c_ulong()))


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.IntegratedPrecisionPiezo.DLL")

IPP_CanDeviceLockFrontPanel = lib.IPP_CanDeviceLockFrontPanel
IPP_CanDeviceLockFrontPanel.restype = c_bool
IPP_CanDeviceLockFrontPanel.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = IPP_CanDeviceLockFrontPanel(serial_number)

    return output


IPP_CheckConnection = lib.IPP_CheckConnection
IPP_CheckConnection.restype = c_bool
IPP_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = IPP_CheckConnection(serial_number)

    return output


IPP_ClearMessageQueue = lib.IPP_ClearMessageQueue
IPP_ClearMessageQueue.restype = c_short
IPP_ClearMessageQueue.argtypes = []


def clear_message_queue(serial_number):
    '''
    Clears the device message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_ClearMessageQueue(serial_number)

    return output


IPP_Close = lib.IPP_Close
IPP_Close.restype = c_void_p
IPP_Close.argtypes = []


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

    output = IPP_Close(serial_number)

    return output


IPP_DisableChannel = lib.IPP_DisableChannel
IPP_DisableChannel.restype = c_short
IPP_DisableChannel.argtypes = []


def disable_channel(serial_number):
    '''
    Disable the channel so that motor can be moved by hand.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_DisableChannel(serial_number)

    return output


IPP_Disconnect = lib.IPP_Disconnect
IPP_Disconnect.restype = c_short
IPP_Disconnect.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = IPP_Disconnect(serial_number)

    return output


IPP_EnableChannel = lib.IPP_EnableChannel
IPP_EnableChannel.restype = c_short
IPP_EnableChannel.argtypes = []


def enable_channel(serial_number):
    '''
    Enable channel for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_EnableChannel(serial_number)

    return output


IPP_GetFirmwareVersion = lib.IPP_GetFirmwareVersion
IPP_GetFirmwareVersion.restype = c_ulong
IPP_GetFirmwareVersion.argtypes = []


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

    output = IPP_GetFirmwareVersion(serial_number)

    return output


IPP_GetFrontPanelLocked = lib.IPP_GetFrontPanelLocked
IPP_GetFrontPanelLocked.restype = c_bool
IPP_GetFrontPanelLocked.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = IPP_GetFrontPanelLocked(serial_number)

    return output


IPP_GetHardwareInfo = lib.IPP_GetHardwareInfo
IPP_GetHardwareInfo.restype = c_short
IPP_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = IPP_GetHardwareInfo(serial_number)

    return output


IPP_GetHardwareInfoBlock = lib.IPP_GetHardwareInfoBlock
IPP_GetHardwareInfoBlock.restype = c_short
IPP_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = IPP_GetHardwareInfoBlock(serial_number)

    return output


IPP_GetIOSettings = lib.IPP_GetIOSettings
IPP_GetIOSettings.restype = c_short
IPP_GetIOSettings.argtypes = []


def get_i_o_settings(serial_number):
    '''
    Gets the PPC IO Settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        ioSettings: PPC_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    ioSettings = PPC_IOSettings()

    output = IPP_GetIOSettings(serial_number)

    return output


IPP_GetMMIParams = lib.IPP_GetMMIParams
IPP_GetMMIParams.restype = c_short
IPP_GetMMIParams.argtypes = []


def get_m_m_i_params(serial_number):
    '''
    Get the MMI Parameters for the Integrated Precision Piezo.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KPZ_WheelMode
        voltageAdjustRate: KPZ_WheelChangeRate
        voltageStep: c_int32
        directionSense: KPZ_WheelDirectionSense
        presetVoltage1: c_int32
        presetVoltage2: c_int32
        displayIntensity: c_int16
        displayTimeout: c_int16
        displayDimIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int32()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int32()
    presetVoltage2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = IPP_GetMMIParams(serial_number)

    return output


IPP_GetMaxOutputVoltage = lib.IPP_GetMaxOutputVoltage
IPP_GetMaxOutputVoltage.restype = c_short
IPP_GetMaxOutputVoltage.argtypes = []


def get_max_output_voltage(serial_number):
    '''
    Gets the maximum output voltage (140V) in units of 1 tenth of a volt

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_GetMaxOutputVoltage(serial_number)

    return output


IPP_GetMinOutputVoltage = lib.IPP_GetMinOutputVoltage
IPP_GetMinOutputVoltage.restype = c_short
IPP_GetMinOutputVoltage.argtypes = []


def get_min_output_voltage(serial_number):
    '''
    Gets the minimum output voltage (-10V) in units of 1 tenth of a volt.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_GetMinOutputVoltage(serial_number)

    return output


IPP_GetNextMessage = lib.IPP_GetNextMessage
IPP_GetNextMessage.restype = c_bool
IPP_GetNextMessage.argtypes = []


def get_next_message(serial_number):
    '''
    Get the next MessageQueue item if it is available.

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

    output = IPP_GetNextMessage(serial_number)

    return output


IPP_GetOutputVoltage = lib.IPP_GetOutputVoltage
IPP_GetOutputVoltage.restype = c_short
IPP_GetOutputVoltage.argtypes = []


def get_output_voltage(serial_number):
    '''
    Gets the set Output Voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_GetOutputVoltage(serial_number)

    return output


IPP_GetPIDConsts = lib.IPP_GetPIDConsts
IPP_GetPIDConsts.restype = c_short
IPP_GetPIDConsts.argtypes = []


def get_p_i_d_consts(serial_number):
    '''
    Gets the PPC PID Constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_byte
        pidConsts: PPC_PIDConsts

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_byte()
    pidConsts = PPC_PIDConsts()

    output = IPP_GetPIDConsts(serial_number)

    return output


IPP_GetPIDCriteria = lib.IPP_GetPIDCriteria
IPP_GetPIDCriteria.restype = c_short
IPP_GetPIDCriteria.argtypes = []


def get_p_i_d_criteria(serial_number):
    '''
    Gets the PID Criteria.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        criteriaID: c_byte
        pidCriteria: PPC_PIDCriteria

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    criteriaID = c_byte()
    pidCriteria = PPC_PIDCriteria()

    output = IPP_GetPIDCriteria(serial_number)

    return output


IPP_GetPosition = lib.IPP_GetPosition
IPP_GetPosition.restype = c_short
IPP_GetPosition.argtypes = []


def get_position(serial_number):
    '''
    Gets the current position Please note this is non linear

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_GetPosition(serial_number)

    return output


IPP_GetPositionControlMode = lib.IPP_GetPositionControlMode
IPP_GetPositionControlMode.restype = PZ_ControlModeTypes
IPP_GetPositionControlMode.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = IPP_GetPositionControlMode(serial_number)

    return output


IPP_GetSoftwareVersion = lib.IPP_GetSoftwareVersion
IPP_GetSoftwareVersion.restype = c_ulong
IPP_GetSoftwareVersion.argtypes = []


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

    output = IPP_GetSoftwareVersion(serial_number)

    return output


IPP_GetStatusBits = lib.IPP_GetStatusBits
IPP_GetStatusBits.restype = c_ulong
IPP_GetStatusBits.argtypes = []


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

    output = IPP_GetStatusBits(serial_number)

    return output


IPP_GetTriggerConfigParams = lib.IPP_GetTriggerConfigParams
IPP_GetTriggerConfigParams.restype = c_short
IPP_GetTriggerConfigParams.argtypes = []


def get_trigger_config_params(serial_number):
    '''
    Get the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KSG_TriggerPortMode
        trigger1Polarity: KSG_TriggerPortPolarity
        trigger2Mode: KSG_TriggerPortMode
        trigger2Polarity: KSG_TriggerPortPolarity
        lowerLimit: c_int32
        upperLimit: c_int32
        smoothingSamples: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    trigger1Mode = KSG_TriggerPortMode()
    trigger1Polarity = KSG_TriggerPortPolarity()
    trigger2Mode = KSG_TriggerPortMode()
    trigger2Polarity = KSG_TriggerPortPolarity()
    lowerLimit = c_int32()
    upperLimit = c_int32()
    smoothingSamples = c_int16()

    output = IPP_GetTriggerConfigParams(serial_number)

    return output


IPP_GetTriggerConfigParamsBlock = lib.IPP_GetTriggerConfigParamsBlock
IPP_GetTriggerConfigParamsBlock.restype = c_short
IPP_GetTriggerConfigParamsBlock.argtypes = []


def get_trigger_config_params_block(serial_number):
    '''
    Gets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KSG_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    triggerConfigParams = KSG_TriggerConfig()

    output = IPP_GetTriggerConfigParamsBlock(serial_number)

    return output


IPP_GetVoltageSource = lib.IPP_GetVoltageSource
IPP_GetVoltageSource.restype = PZ_InputSourceFlags
IPP_GetVoltageSource.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = IPP_GetVoltageSource(serial_number)

    return output


IPP_Identify = lib.IPP_Identify
IPP_Identify.restype = c_void_p
IPP_Identify.argtypes = []


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

    output = IPP_Identify(serial_number)

    return output


IPP_LoadNamedSettings = lib.IPP_LoadNamedSettings
IPP_LoadNamedSettings.restype = c_bool
IPP_LoadNamedSettings.argtypes = []


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

    output = IPP_LoadNamedSettings(serial_number)

    return output


IPP_LoadSettings = lib.IPP_LoadSettings
IPP_LoadSettings.restype = c_bool
IPP_LoadSettings.argtypes = []


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

    output = IPP_LoadSettings(serial_number)

    return output


IPP_MessageQueueSize = lib.IPP_MessageQueueSize
IPP_MessageQueueSize.restype = c_int
IPP_MessageQueueSize.argtypes = []


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

    output = IPP_MessageQueueSize(serial_number)

    return output


IPP_Open = lib.IPP_Open
IPP_Open.restype = c_short
IPP_Open.argtypes = []


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

    output = IPP_Open(serial_number)

    return output


IPP_PersistSettings = lib.IPP_PersistSettings
IPP_PersistSettings.restype = c_bool
IPP_PersistSettings.argtypes = []


def persist_settings(serial_number):
    '''
    Persist device settings to device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_PersistSettings(serial_number)

    return output


IPP_PollingDuration = lib.IPP_PollingDuration
IPP_PollingDuration.restype = c_long
IPP_PollingDuration.argtypes = []


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

    output = IPP_PollingDuration(serial_number)

    return output


IPP_RegisterMessageCallback = lib.IPP_RegisterMessageCallback
IPP_RegisterMessageCallback.restype = c_short
IPP_RegisterMessageCallback.argtypes = []


def register_message_callback(serial_number):
    '''
    Registers a callback on the message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        None

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RegisterMessageCallback(serial_number)

    return output


IPP_RequestFrontPanelLocked = lib.IPP_RequestFrontPanelLocked
IPP_RequestFrontPanelLocked.restype = c_short
IPP_RequestFrontPanelLocked.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestFrontPanelLocked(serial_number)

    return output


IPP_RequestIOSettings = lib.IPP_RequestIOSettings
IPP_RequestIOSettings.restype = c_bool
IPP_RequestIOSettings.argtypes = []


def request_i_o_settings(serial_number):
    '''
    Requests the curent PPC IO Setting.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestIOSettings(serial_number)

    return output


IPP_RequestMMIParams = lib.IPP_RequestMMIParams
IPP_RequestMMIParams.restype = c_bool
IPP_RequestMMIParams.argtypes = []


def request_m_m_i_params(serial_number):
    '''
    Request that the MMI Parameters for the Integrated Precision Piezo be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestMMIParams(serial_number)

    return output


IPP_RequestOutputVoltage = lib.IPP_RequestOutputVoltage
IPP_RequestOutputVoltage.restype = c_bool
IPP_RequestOutputVoltage.argtypes = []


def request_output_voltage(serial_number):
    '''
    Requests the maximum output voltage be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestOutputVoltage(serial_number)

    return output


IPP_RequestPIDConsts = lib.IPP_RequestPIDConsts
IPP_RequestPIDConsts.restype = c_short
IPP_RequestPIDConsts.argtypes = []


def request_p_i_d_consts(serial_number):
    '''
    Requests the PID Constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_byte()

    output = IPP_RequestPIDConsts(serial_number)

    return output


IPP_RequestPIDCriteria = lib.IPP_RequestPIDCriteria
IPP_RequestPIDCriteria.restype = c_short
IPP_RequestPIDCriteria.argtypes = []


def request_p_i_d_criteria(serial_number):
    '''
    Requests the PID Criteria.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        criteriaID: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    criteriaID = c_byte()

    output = IPP_RequestPIDCriteria(serial_number)

    return output


IPP_RequestPosition = lib.IPP_RequestPosition
IPP_RequestPosition.restype = c_bool
IPP_RequestPosition.argtypes = []


def request_position(serial_number):
    '''
    Gets the current Closed Loop position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestPosition(serial_number)

    return output


IPP_RequestPositionControlMode = lib.IPP_RequestPositionControlMode
IPP_RequestPositionControlMode.restype = c_bool
IPP_RequestPositionControlMode.argtypes = []


def request_position_control_mode(serial_number):
    '''
    Requests that the Position Control Mode be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestPositionControlMode(serial_number)

    return output


IPP_RequestSettings = lib.IPP_RequestSettings
IPP_RequestSettings.restype = c_short
IPP_RequestSettings.argtypes = []


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

    output = IPP_RequestSettings(serial_number)

    return output


IPP_RequestStatus = lib.IPP_RequestStatus
IPP_RequestStatus.restype = c_short
IPP_RequestStatus.argtypes = []


def request_status(serial_number):
    '''
    Requests the status bits and position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestStatus(serial_number)

    return output


IPP_RequestStatusBits = lib.IPP_RequestStatusBits
IPP_RequestStatusBits.restype = c_short
IPP_RequestStatusBits.argtypes = []


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

    output = IPP_RequestStatusBits(serial_number)

    return output


IPP_RequestTriggerConfigParams = lib.IPP_RequestTriggerConfigParams
IPP_RequestTriggerConfigParams.restype = c_short
IPP_RequestTriggerConfigParams.argtypes = []


def request_trigger_config_params(serial_number):
    '''
    Requests the trigger config parameters

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestTriggerConfigParams(serial_number)

    return output


IPP_RequestVoltageSource = lib.IPP_RequestVoltageSource
IPP_RequestVoltageSource.restype = c_bool
IPP_RequestVoltageSource.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = IPP_RequestVoltageSource(serial_number)

    return output


IPP_ResetParameters = lib.IPP_ResetParameters
IPP_ResetParameters.restype = c_short
IPP_ResetParameters.argtypes = []


def reset_parameters(serial_number):
    '''
    Sets the voltage output to zero and defines the ensuing actuator position az zero.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_ResetParameters(serial_number)

    return output


IPP_SetFrontPanelLock = lib.IPP_SetFrontPanelLock
IPP_SetFrontPanelLock.restype = c_short
IPP_SetFrontPanelLock.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    locked = c_bool()

    output = IPP_SetFrontPanelLock(serial_number)

    return output


IPP_SetIOSettings = lib.IPP_SetIOSettings
IPP_SetIOSettings.restype = c_short
IPP_SetIOSettings.argtypes = []


def set_i_o_settings(serial_number):
    '''
    Sets the PPC IO Setting.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        ioSettings: PPC_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    ioSettings = PPC_IOSettings()

    output = IPP_SetIOSettings(serial_number)

    return output


IPP_SetMMIParams = lib.IPP_SetMMIParams
IPP_SetMMIParams.restype = c_short
IPP_SetMMIParams.argtypes = []


def set_m_m_i_params(serial_number):
    '''
    Set the MMI Parameters for the Integrated PrecisionPiezo.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelMode: KPZ_WheelMode
        voltageAdjustRate: KPZ_WheelChangeRate
        voltageStep: c_int32
        directionSense: KPZ_WheelDirectionSense
        presetVoltage1: c_int32
        presetVoltage2: c_int32
        displayIntensity: c_int16
        displayTimeout: c_int16
        displayDimIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    wheelMode = KPZ_WheelMode()
    voltageAdjustRate = KPZ_WheelChangeRate()
    voltageStep = c_int32()
    directionSense = KPZ_WheelDirectionSense()
    presetVoltage1 = c_int32()
    presetVoltage2 = c_int32()
    displayIntensity = c_int16()
    displayTimeout = c_int16()
    displayDimIntensity = c_int16()

    output = IPP_SetMMIParams(serial_number)

    return output


IPP_SetOutputVoltage = lib.IPP_SetOutputVoltage
IPP_SetOutputVoltage.restype = c_short
IPP_SetOutputVoltage.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    volts = c_short()

    output = IPP_SetOutputVoltage(serial_number)

    return output


IPP_SetPIDConsts = lib.IPP_SetPIDConsts
IPP_SetPIDConsts.restype = c_short
IPP_SetPIDConsts.argtypes = []


def set_p_i_d_consts(serial_number):
    '''
    Sets the PPC PID Constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        pidConsts: PPC_PIDConsts

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    pidConsts = PPC_PIDConsts()

    output = IPP_SetPIDConsts(serial_number)

    return output


IPP_SetPIDCriteria = lib.IPP_SetPIDCriteria
IPP_SetPIDCriteria.restype = c_short
IPP_SetPIDCriteria.argtypes = []


def set_p_i_d_criteria(serial_number):
    '''
    Sets the PID Criteria.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        pidCriteria: PPC_PIDCriteria

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    pidCriteria = PPC_PIDCriteria()

    output = IPP_SetPIDCriteria(serial_number)

    return output


IPP_SetPosition = lib.IPP_SetPosition
IPP_SetPosition.restype = c_short
IPP_SetPosition.argtypes = []


def set_position(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    position = c_short()

    output = IPP_SetPosition(serial_number)

    return output


IPP_SetPositionControlMode = lib.IPP_SetPositionControlMode
IPP_SetPositionControlMode.restype = c_short
IPP_SetPositionControlMode.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    mode = PZ_ControlModeTypes()

    output = IPP_SetPositionControlMode(serial_number)

    return output


IPP_SetTriggerConfigParams = lib.IPP_SetTriggerConfigParams
IPP_SetTriggerConfigParams.restype = c_short
IPP_SetTriggerConfigParams.argtypes = []


def set_trigger_config_params(serial_number):
    '''
    Set the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KSG_TriggerPortMode
        trigger1Polarity: KSG_TriggerPortPolarity
        trigger2Mode: KSG_TriggerPortMode
        trigger2Polarity: KSG_TriggerPortPolarity
        lowerLimit: c_int32
        upperLimit: c_int32
        smoothingSamples: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    trigger1Mode = KSG_TriggerPortMode()
    trigger1Polarity = KSG_TriggerPortPolarity()
    trigger2Mode = KSG_TriggerPortMode()
    trigger2Polarity = KSG_TriggerPortPolarity()
    lowerLimit = c_int32()
    upperLimit = c_int32()
    smoothingSamples = c_int16()

    output = IPP_SetTriggerConfigParams(serial_number)

    return output


IPP_SetTriggerConfigParamsBlock = lib.IPP_SetTriggerConfigParamsBlock
IPP_SetTriggerConfigParamsBlock.restype = c_short
IPP_SetTriggerConfigParamsBlock.argtypes = []


def set_trigger_config_params_block(serial_number):
    '''
    Sets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KSG_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    triggerConfigParams = KSG_TriggerConfig()

    output = IPP_SetTriggerConfigParamsBlock(serial_number)

    return output


IPP_SetVoltageSource = lib.IPP_SetVoltageSource
IPP_SetVoltageSource.restype = c_short
IPP_SetVoltageSource.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    source = PZ_InputSourceFlags()

    output = IPP_SetVoltageSource(serial_number)

    return output


IPP_SetZero = lib.IPP_SetZero
IPP_SetZero.restype = c_short
IPP_SetZero.argtypes = []


def set_zero(serial_number):
    '''
    Performs a Set Zero operation.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = IPP_SetZero(serial_number)

    return output


IPP_StartPolling = lib.IPP_StartPolling
IPP_StartPolling.restype = c_bool
IPP_StartPolling.argtypes = []


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

    output = IPP_StartPolling(serial_number)

    return output


IPP_StopPolling = lib.IPP_StopPolling
IPP_StopPolling.restype = c_void_p
IPP_StopPolling.argtypes = []


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

    output = IPP_StopPolling(serial_number)

    return output


IPP_WaitForMessage = lib.IPP_WaitForMessage
IPP_WaitForMessage.restype = c_bool
IPP_WaitForMessage.argtypes = []


def wait_for_message(serial_number):
    '''
    Get the next MessageQueue item if it is available.

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

    output = IPP_WaitForMessage(serial_number)

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



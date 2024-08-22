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
    HubAnalogueModes,
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
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
    lib_path + "Thorlabs.MotionControl.TCube.Piezo.DLL")

PCC_CheckConnection = lib.PCC_CheckConnection
PCC_CheckConnection.restype = c_bool
PCC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = PCC_CheckConnection(serial_number)

    return output


PCC_ClearMessageQueue = lib.PCC_ClearMessageQueue
PCC_ClearMessageQueue.restype = c_void_p
PCC_ClearMessageQueue.argtypes = [POINTER(c_char)]


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

    output = PCC_ClearMessageQueue(serial_number)

    return output


PCC_Close = lib.PCC_Close
PCC_Close.restype = c_void_p
PCC_Close.argtypes = [POINTER(c_char)]


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

    output = PCC_Close(serial_number)

    return output


PCC_Disable = lib.PCC_Disable
PCC_Disable.restype = c_short
PCC_Disable.argtypes = [POINTER(c_char)]


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

    output = PCC_Disable(serial_number)

    return output


PCC_Disconnect = lib.PCC_Disconnect
PCC_Disconnect.restype = c_short
PCC_Disconnect.argtypes = [POINTER(c_char)]


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

    output = PCC_Disconnect(serial_number)

    return output


PCC_Enable = lib.PCC_Enable
PCC_Enable.restype = c_short
PCC_Enable.argtypes = [POINTER(c_char)]


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

    output = PCC_Enable(serial_number)

    return output


PCC_EnableLastMsgTimer = lib.PCC_EnableLastMsgTimer
PCC_EnableLastMsgTimer.restype = c_void_p
PCC_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


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

    output = PCC_EnableLastMsgTimer(serial_number)

    return output


PCC_GetFeedbackLoopPIconsts = lib.PCC_GetFeedbackLoopPIconsts
PCC_GetFeedbackLoopPIconsts.restype = c_short
PCC_GetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def get_feedback_loop_p_iconsts(serial_number):
    '''
    Gets the feedback loop parameters.

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

    output = PCC_GetFeedbackLoopPIconsts(serial_number)

    return output


PCC_GetFeedbackLoopPIconstsBlock = lib.PCC_GetFeedbackLoopPIconstsBlock
PCC_GetFeedbackLoopPIconstsBlock.restype = c_short
PCC_GetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


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

    output = PCC_GetFeedbackLoopPIconstsBlock(serial_number)

    return output


PCC_GetFirmwareVersion = lib.PCC_GetFirmwareVersion
PCC_GetFirmwareVersion.restype = c_ulong
PCC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


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

    output = PCC_GetFirmwareVersion(serial_number)

    return output


PCC_GetHardwareInfo = lib.PCC_GetHardwareInfo
PCC_GetHardwareInfo.restype = c_short
PCC_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = PCC_GetHardwareInfo(serial_number)

    return output


PCC_GetHardwareInfoBlock = lib.PCC_GetHardwareInfoBlock
PCC_GetHardwareInfoBlock.restype = c_short
PCC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = PCC_GetHardwareInfoBlock(serial_number)

    return output


PCC_GetHubAnalogInput = lib.PCC_GetHubAnalogInput
PCC_GetHubAnalogInput.restype = HubAnalogueModes
PCC_GetHubAnalogInput.argtypes = [POINTER(c_char)]


def get_hub_analog_input(serial_number):
    '''
    Gets the Hub Analog Input.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        HubAnalogueModes
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetHubAnalogInput(serial_number)

    return output


PCC_GetIOSettings = lib.PCC_GetIOSettings
PCC_GetIOSettings.restype = TPZ_IOSettings
PCC_GetIOSettings.argtypes = [POINTER(c_char)]


def get_i_o_settings(serial_number):
    '''
    Gets the IO settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        TPZ_IOSettings
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetIOSettings(serial_number)

    return output


PCC_GetLEDBrightness = lib.PCC_GetLEDBrightness
PCC_GetLEDBrightness.restype = c_short
PCC_GetLEDBrightness.argtypes = [POINTER(c_char)]


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

    output = PCC_GetLEDBrightness(serial_number)

    return output


PCC_GetMaxOutputVoltage = lib.PCC_GetMaxOutputVoltage
PCC_GetMaxOutputVoltage.restype = c_short
PCC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


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

    output = PCC_GetMaxOutputVoltage(serial_number)

    return output


PCC_GetNextMessage = lib.PCC_GetNextMessage
PCC_GetNextMessage.restype = c_bool
PCC_GetNextMessage.argtypes = [POINTER(c_char)]


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

    output = PCC_GetNextMessage(serial_number)

    return output


PCC_GetOutputVoltage = lib.PCC_GetOutputVoltage
PCC_GetOutputVoltage.restype = c_short
PCC_GetOutputVoltage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_GetOutputVoltage(serial_number)

    return output


PCC_GetPosition = lib.PCC_GetPosition
PCC_GetPosition.restype = c_long
PCC_GetPosition.argtypes = [POINTER(c_char)]


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

    output = PCC_GetPosition(serial_number)

    return output


PCC_GetPositionControlMode = lib.PCC_GetPositionControlMode
PCC_GetPositionControlMode.restype = PZ_ControlModeTypes
PCC_GetPositionControlMode.argtypes = [POINTER(c_char)]


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

    output = PCC_GetPositionControlMode(serial_number)

    return output


PCC_GetSoftwareVersion = lib.PCC_GetSoftwareVersion
PCC_GetSoftwareVersion.restype = c_ulong
PCC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    output = PCC_GetSoftwareVersion(serial_number)

    return output


PCC_GetStatusBits = lib.PCC_GetStatusBits
PCC_GetStatusBits.restype = c_ulong
PCC_GetStatusBits.argtypes = [POINTER(c_char)]


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

    output = PCC_GetStatusBits(serial_number)

    return output


PCC_GetVoltageSource = lib.PCC_GetVoltageSource
PCC_GetVoltageSource.restype = PZ_InputSourceFlags
PCC_GetVoltageSource.argtypes = [POINTER(c_char)]


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

    output = PCC_GetVoltageSource(serial_number)

    return output


PCC_HasLastMsgTimerOverrun = lib.PCC_HasLastMsgTimerOverrun
PCC_HasLastMsgTimerOverrun.restype = c_bool
PCC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by PCC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_HasLastMsgTimerOverrun(serial_number)

    return output


PCC_Identify = lib.PCC_Identify
PCC_Identify.restype = c_void_p
PCC_Identify.argtypes = [POINTER(c_char)]


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

    output = PCC_Identify(serial_number)

    return output


PCC_LoadNamedSettings = lib.PCC_LoadNamedSettings
PCC_LoadNamedSettings.restype = c_bool
PCC_LoadNamedSettings.argtypes = [POINTER(c_char)]


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

    output = PCC_LoadNamedSettings(serial_number)

    return output


PCC_LoadSettings = lib.PCC_LoadSettings
PCC_LoadSettings.restype = c_bool
PCC_LoadSettings.argtypes = [POINTER(c_char)]


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

    output = PCC_LoadSettings(serial_number)

    return output


PCC_MessageQueueSize = lib.PCC_MessageQueueSize
PCC_MessageQueueSize.restype = c_int
PCC_MessageQueueSize.argtypes = [POINTER(c_char)]


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

    output = PCC_MessageQueueSize(serial_number)

    return output


PCC_Open = lib.PCC_Open
PCC_Open.restype = c_short
PCC_Open.argtypes = [POINTER(c_char)]


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

    output = PCC_Open(serial_number)

    return output


PCC_PersistSettings = lib.PCC_PersistSettings
PCC_PersistSettings.restype = c_bool
PCC_PersistSettings.argtypes = [POINTER(c_char)]


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

    output = PCC_PersistSettings(serial_number)

    return output


PCC_PollingDuration = lib.PCC_PollingDuration
PCC_PollingDuration.restype = c_long
PCC_PollingDuration.argtypes = [POINTER(c_char)]


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

    output = PCC_PollingDuration(serial_number)

    return output


PCC_RegisterMessageCallback = lib.PCC_RegisterMessageCallback
PCC_RegisterMessageCallback.restype = c_void_p
PCC_RegisterMessageCallback.argtypes = [POINTER(c_char)]


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

    output = PCC_RegisterMessageCallback(serial_number)

    return output


PCC_RequestFeedbackLoopPIconsts = lib.PCC_RequestFeedbackLoopPIconsts
PCC_RequestFeedbackLoopPIconsts.restype = c_bool
PCC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestFeedbackLoopPIconsts(serial_number)

    return output


PCC_RequestIOSettings = lib.PCC_RequestIOSettings
PCC_RequestIOSettings.restype = c_bool
PCC_RequestIOSettings.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestIOSettings(serial_number)

    return output


PCC_RequestLEDBrightness = lib.PCC_RequestLEDBrightness
PCC_RequestLEDBrightness.restype = c_bool
PCC_RequestLEDBrightness.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestLEDBrightness(serial_number)

    return output


PCC_RequestPosition = lib.PCC_RequestPosition
PCC_RequestPosition.restype = c_short
PCC_RequestPosition.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestPosition(serial_number)

    return output


PCC_RequestPositionControlMode = lib.PCC_RequestPositionControlMode
PCC_RequestPositionControlMode.restype = c_short
PCC_RequestPositionControlMode.argtypes = [POINTER(c_char)]


def request_position_control_mode(serial_number):
    '''
    Requests that the Position Control Mode be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PCC_RequestPositionControlMode(serial_number)

    return output


PCC_RequestSettings = lib.PCC_RequestSettings
PCC_RequestSettings.restype = c_short
PCC_RequestSettings.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestSettings(serial_number)

    return output


PCC_RequestStatus = lib.PCC_RequestStatus
PCC_RequestStatus.restype = c_short
PCC_RequestStatus.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestStatus(serial_number)

    return output


PCC_RequestStatusBits = lib.PCC_RequestStatusBits
PCC_RequestStatusBits.restype = c_short
PCC_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestStatusBits(serial_number)

    return output


PCC_RequestVoltageSource = lib.PCC_RequestVoltageSource
PCC_RequestVoltageSource.restype = c_bool
PCC_RequestVoltageSource.argtypes = [POINTER(c_char)]


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

    output = PCC_RequestVoltageSource(serial_number)

    return output


PCC_SetFeedbackLoopPIconsts = lib.PCC_SetFeedbackLoopPIconsts
PCC_SetFeedbackLoopPIconsts.restype = c_short
PCC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


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

    output = PCC_SetFeedbackLoopPIconsts(serial_number)

    return output


PCC_SetFeedbackLoopPIconstsBlock = lib.PCC_SetFeedbackLoopPIconstsBlock
PCC_SetFeedbackLoopPIconstsBlock.restype = c_short
PCC_SetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


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

    output = PCC_SetFeedbackLoopPIconstsBlock(serial_number)

    return output


PCC_SetHubAnalogInput = lib.PCC_SetHubAnalogInput
PCC_SetHubAnalogInput.restype = c_short
PCC_SetHubAnalogInput.argtypes = [POINTER(c_char)]


def set_hub_analog_input(serial_number):
    '''
    Sets the Hub Analog Input.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        hubAnalogInput: HubAnalogueModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    hubAnalogInput = HubAnalogueModes()

    output = PCC_SetHubAnalogInput(serial_number)

    return output


PCC_SetIOSettings = lib.PCC_SetIOSettings
PCC_SetIOSettings.restype = c_short
PCC_SetIOSettings.argtypes = [POINTER(c_char)]


def set_i_o_settings(serial_number):
    '''
    Sets the IO settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        ioSettings: TPZ_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    ioSettings = TPZ_IOSettings()

    output = PCC_SetIOSettings(serial_number)

    return output


PCC_SetLEDBrightness = lib.PCC_SetLEDBrightness
PCC_SetLEDBrightness.restype = c_short
PCC_SetLEDBrightness.argtypes = [POINTER(c_char)]


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

    output = PCC_SetLEDBrightness(serial_number)

    return output


PCC_SetLUTwaveParams = lib.PCC_SetLUTwaveParams
PCC_SetLUTwaveParams.restype = c_short
PCC_SetLUTwaveParams.argtypes = [POINTER(c_char)]


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

    output = PCC_SetLUTwaveParams(serial_number)

    return output


PCC_SetLUTwaveSample = lib.PCC_SetLUTwaveSample
PCC_SetLUTwaveSample.restype = c_short
PCC_SetLUTwaveSample.argtypes = [POINTER(c_char)]


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

    output = PCC_SetLUTwaveSample(serial_number)

    return output


PCC_SetMaxOutputVoltage = lib.PCC_SetMaxOutputVoltage
PCC_SetMaxOutputVoltage.restype = c_short
PCC_SetMaxOutputVoltage.argtypes = [POINTER(c_char)]


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

    output = PCC_SetMaxOutputVoltage(serial_number)

    return output


PCC_SetOutputVoltage = lib.PCC_SetOutputVoltage
PCC_SetOutputVoltage.restype = c_short
PCC_SetOutputVoltage.argtypes = [POINTER(c_char)]


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

    output = PCC_SetOutputVoltage(serial_number)

    return output


PCC_SetPosition = lib.PCC_SetPosition
PCC_SetPosition.restype = c_short
PCC_SetPosition.argtypes = [POINTER(c_char)]


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

    output = PCC_SetPosition(serial_number)

    return output


PCC_SetPositionControlMode = lib.PCC_SetPositionControlMode
PCC_SetPositionControlMode.restype = c_short
PCC_SetPositionControlMode.argtypes = [POINTER(c_char)]


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

    output = PCC_SetPositionControlMode(serial_number)

    return output


PCC_SetPositionToTolerance = lib.PCC_SetPositionToTolerance
PCC_SetPositionToTolerance.restype = c_short
PCC_SetPositionToTolerance.argtypes = [POINTER(c_char)]


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

    output = PCC_SetPositionToTolerance(serial_number)

    return output


PCC_SetVoltageSource = lib.PCC_SetVoltageSource
PCC_SetVoltageSource.restype = c_short
PCC_SetVoltageSource.argtypes = [POINTER(c_char)]


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

    output = PCC_SetVoltageSource(serial_number)

    return output


PCC_SetZero = lib.PCC_SetZero
PCC_SetZero.restype = c_bool
PCC_SetZero.argtypes = [POINTER(c_char)]


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

    output = PCC_SetZero(serial_number)

    return output


PCC_StartLUTwave = lib.PCC_StartLUTwave
PCC_StartLUTwave.restype = c_short
PCC_StartLUTwave.argtypes = [POINTER(c_char)]


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

    output = PCC_StartLUTwave(serial_number)

    return output


PCC_StartPolling = lib.PCC_StartPolling
PCC_StartPolling.restype = c_bool
PCC_StartPolling.argtypes = [POINTER(c_char)]


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

    output = PCC_StartPolling(serial_number)

    return output


PCC_StopLUTwave = lib.PCC_StopLUTwave
PCC_StopLUTwave.restype = c_short
PCC_StopLUTwave.argtypes = [POINTER(c_char)]


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

    output = PCC_StopLUTwave(serial_number)

    return output


PCC_StopPolling = lib.PCC_StopPolling
PCC_StopPolling.restype = c_void_p
PCC_StopPolling.argtypes = [POINTER(c_char)]


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

    output = PCC_StopPolling(serial_number)

    return output


PCC_TimeSinceLastMsgReceived = lib.PCC_TimeSinceLastMsgReceived
PCC_TimeSinceLastMsgReceived.restype = c_bool
PCC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


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

    output = PCC_TimeSinceLastMsgReceived(serial_number)

    return output


PCC_WaitForMessage = lib.PCC_WaitForMessage
PCC_WaitForMessage.restype = c_bool
PCC_WaitForMessage.argtypes = [POINTER(c_char)]


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

    output = PCC_WaitForMessage(serial_number)

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



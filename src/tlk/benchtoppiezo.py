from ctypes import (
    POINTER,
    c_bool,
    c_byte,
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
    PZ_ControlModeTypes,
    PZ_InputSourceFlags)
from .definitions.structures import (
    PZ_FeedbackLoopConstants,
    PZ_LUTWaveParameters,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Benchtop.Piezo.dll")

PBC_CheckConnection = lib.PBC_CheckConnection
PBC_CheckConnection.restype = c_bool
PBC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = PBC_CheckConnection(serial_number)

    return output


PBC_ClearMessageQueue = lib.PBC_ClearMessageQueue
PBC_ClearMessageQueue.restype = c_short
PBC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    '''
    Clears the device message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_ClearMessageQueue(serial_number)

    return output


PBC_Close = lib.PBC_Close
PBC_Close.restype = c_void_p
PBC_Close.argtypes = [POINTER(c_char)]


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

    output = PBC_Close(serial_number)

    return output


PBC_DisableChannel = lib.PBC_DisableChannel
PBC_DisableChannel.restype = c_short
PBC_DisableChannel.argtypes = [POINTER(c_char)]


def disable_channel(serial_number):
    '''
    Disable the channel so that motor can be moved by hand.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_DisableChannel(serial_number)

    return output


PBC_Disconnect = lib.PBC_Disconnect
PBC_Disconnect.restype = c_short
PBC_Disconnect.argtypes = [POINTER(c_char)]


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

    output = PBC_Disconnect(serial_number)

    return output


PBC_EnableChannel = lib.PBC_EnableChannel
PBC_EnableChannel.restype = c_short
PBC_EnableChannel.argtypes = [POINTER(c_char)]


def enable_channel(serial_number):
    '''
    Enable channel for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_EnableChannel(serial_number)

    return output


PBC_EnableLastMsgTimer = lib.PBC_EnableLastMsgTimer
PBC_EnableLastMsgTimer.restype = c_void_p
PBC_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


def enable_last_msg_timer(serial_number):
    '''
    Enables the last message monitoring timer.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        enable: c_bool
        lastMsgTimeout: c_int32

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = PBC_EnableLastMsgTimer(serial_number)

    return output


PBC_GetFeedbackLoopPIconsts = lib.PBC_GetFeedbackLoopPIconsts
PBC_GetFeedbackLoopPIconsts.restype = c_short
PBC_GetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def get_feedback_loop_p_iconsts(serial_number):
    '''
    Gets the feedback loop parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        proportionalTerm: c_short
        integralTerm: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = PBC_GetFeedbackLoopPIconsts(serial_number)

    return output


PBC_GetFeedbackLoopPIconstsBlock = lib.PBC_GetFeedbackLoopPIconstsBlock
PBC_GetFeedbackLoopPIconstsBlock.restype = c_short
PBC_GetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


def get_feedback_loop_p_iconsts_block(serial_number):
    '''
    Gets the feedback loop constants in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        proportionalAndIntegralConstants: PZ_FeedbackLoopConstants

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PBC_GetFeedbackLoopPIconstsBlock(serial_number)

    return output


PBC_GetFirmwareVersion = lib.PBC_GetFirmwareVersion
PBC_GetFirmwareVersion.restype = c_ulong
PBC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


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

    output = PBC_GetFirmwareVersion(serial_number)

    return output


PBC_GetHardwareInfo = lib.PBC_GetHardwareInfo
PBC_GetHardwareInfo.restype = c_short
PBC_GetHardwareInfo.argtypes = [POINTER(c_char)]


def get_hardware_info(serial_number):
    '''
    Gets the hardware information from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
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
    channel = c_short()
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = PBC_GetHardwareInfo(serial_number)

    return output


PBC_GetHardwareInfoBlock = lib.PBC_GetHardwareInfoBlock
PBC_GetHardwareInfoBlock.restype = c_short
PBC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


def get_hardware_info_block(serial_number):
    '''
    Gets the hardware information in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        hardwareInfo: TLI_HardwareInformation

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    hardwareInfo = TLI_HardwareInformation()

    output = PBC_GetHardwareInfoBlock(serial_number)

    return output


PBC_GetMaxOutputVoltage = lib.PBC_GetMaxOutputVoltage
PBC_GetMaxOutputVoltage.restype = c_short
PBC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def get_max_output_voltage(serial_number):
    '''
    Gets the maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_GetMaxOutputVoltage(serial_number)

    return output


PBC_GetMaximumTravel = lib.PBC_GetMaximumTravel
PBC_GetMaximumTravel.restype = c_long
PBC_GetMaximumTravel.argtypes = [POINTER(c_char)]


def get_maximum_travel(serial_number):
    '''
    Gets the maximum travel of the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_GetMaximumTravel(serial_number)

    return output


PBC_GetNextMessage = lib.PBC_GetNextMessage
PBC_GetNextMessage.restype = c_bool
PBC_GetNextMessage.argtypes = [POINTER(c_char)]


def get_next_message(serial_number):
    '''
    Get the next MessageQueue item if it is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PBC_GetNextMessage(serial_number)

    return output


PBC_GetNumChannels = lib.PBC_GetNumChannels
PBC_GetNumChannels.restype = c_short
PBC_GetNumChannels.argtypes = [POINTER(c_char)]


def get_num_channels(serial_number):
    '''
    Gets the number of channels in the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PBC_GetNumChannels(serial_number)

    return output


PBC_GetOutputVoltage = lib.PBC_GetOutputVoltage
PBC_GetOutputVoltage.restype = c_short
PBC_GetOutputVoltage.argtypes = [POINTER(c_char)]


def get_output_voltage(serial_number):
    '''
    Gets the set Output Voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_GetOutputVoltage(serial_number)

    return output


PBC_GetPosition = lib.PBC_GetPosition
PBC_GetPosition.restype = c_short
PBC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    '''
    Gets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_GetPosition(serial_number)

    return output


PBC_GetPositionControlMode = lib.PBC_GetPositionControlMode
PBC_GetPositionControlMode.restype = PZ_ControlModeTypes
PBC_GetPositionControlMode.argtypes = [POINTER(c_char)]


def get_position_control_mode(serial_number):
    '''
    Gets the Position Control Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        PZ_ControlModeTypes
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_GetPositionControlMode(serial_number)

    return output


PBC_GetRackDigitalOutputs = lib.PBC_GetRackDigitalOutputs
PBC_GetRackDigitalOutputs.restype = c_byte
PBC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def get_rack_digital_outputs(serial_number):
    '''
    Gets the rack digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PBC_GetRackDigitalOutputs(serial_number)

    return output


PBC_GetRackStatusBits = lib.PBC_GetRackStatusBits
PBC_GetRackStatusBits.restype = c_ulong
PBC_GetRackStatusBits.argtypes = [POINTER(c_char)]


def get_rack_status_bits(serial_number):
    '''
    Gets the Rack status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PBC_GetRackStatusBits(serial_number)

    return output


PBC_GetSoftwareVersion = lib.PBC_GetSoftwareVersion
PBC_GetSoftwareVersion.restype = c_ulong
PBC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    output = PBC_GetSoftwareVersion(serial_number)

    return output


PBC_GetStatusBits = lib.PBC_GetStatusBits
PBC_GetStatusBits.restype = c_ulong
PBC_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits(serial_number):
    '''
    Get the current status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_GetStatusBits(serial_number)

    return output


PBC_GetVoltageSource = lib.PBC_GetVoltageSource
PBC_GetVoltageSource.restype = PZ_InputSourceFlags
PBC_GetVoltageSource.argtypes = [POINTER(c_char)]


def get_voltage_source(serial_number):
    '''
    Gets the control voltage source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        PZ_InputSourceFlags
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_GetVoltageSource(serial_number)

    return output


PBC_HasLastMsgTimerOverrun = lib.PBC_HasLastMsgTimerOverrun
PBC_HasLastMsgTimerOverrun.restype = c_bool
PBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by PBC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_HasLastMsgTimerOverrun(serial_number)

    return output


PBC_Identify = lib.PBC_Identify
PBC_Identify.restype = c_void_p
PBC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    '''
    Sends a command to the device to make it identify iteself.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_Identify(serial_number)

    return output


PBC_IsChannelValid = lib.PBC_IsChannelValid
PBC_IsChannelValid.restype = c_bool
PBC_IsChannelValid.argtypes = [POINTER(c_char)]


def is_channel_valid(serial_number):
    '''
    Verifies that the specified channel is valid.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_IsChannelValid(serial_number)

    return output


PBC_LoadNamedSettings = lib.PBC_LoadNamedSettings
PBC_LoadNamedSettings.restype = c_bool
PBC_LoadNamedSettings.argtypes = [POINTER(c_char)]


def load_named_settings(serial_number):
    '''
    Update device with named settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        settingsName: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    settingsName = POINTER(c_char)()

    output = PBC_LoadNamedSettings(serial_number)

    return output


PBC_LoadSettings = lib.PBC_LoadSettings
PBC_LoadSettings.restype = c_bool
PBC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    '''
    Update device with stored settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_LoadSettings(serial_number)

    return output


PBC_MaxChannelCount = lib.PBC_MaxChannelCount
PBC_MaxChannelCount.restype = c_int
PBC_MaxChannelCount.argtypes = [POINTER(c_char)]


def max_channel_count(serial_number):
    '''
    Gets the number of channels available to this device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PBC_MaxChannelCount(serial_number)

    return output


PBC_MessageQueueSize = lib.PBC_MessageQueueSize
PBC_MessageQueueSize.restype = c_int
PBC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    '''
    Gets the MessageQueue size.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_int
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_MessageQueueSize(serial_number)

    return output


PBC_Open = lib.PBC_Open
PBC_Open.restype = c_short
PBC_Open.argtypes = [POINTER(c_char)]


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

    output = PBC_Open(serial_number)

    return output


PBC_PersistSettings = lib.PBC_PersistSettings
PBC_PersistSettings.restype = c_bool
PBC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    '''
    Persist device settings to device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_PersistSettings(serial_number)

    return output


PBC_PollingDuration = lib.PBC_PollingDuration
PBC_PollingDuration.restype = c_long
PBC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    '''
    Gets the polling loop duration.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_PollingDuration(serial_number)

    return output


PBC_RegisterMessageCallback = lib.PBC_RegisterMessageCallback
PBC_RegisterMessageCallback.restype = c_short
PBC_RegisterMessageCallback.argtypes = [POINTER(c_char)]


def register_message_callback(serial_number):
    '''
    Registers a callback on the message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        None

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RegisterMessageCallback(serial_number)

    return output


PBC_RequestActualPosition = lib.PBC_RequestActualPosition
PBC_RequestActualPosition.restype = c_short
PBC_RequestActualPosition.argtypes = [POINTER(c_char)]


def request_actual_position(serial_number):
    '''
    Requests the position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestActualPosition(serial_number)

    return output


PBC_RequestFeedbackLoopPIconsts = lib.PBC_RequestFeedbackLoopPIconsts
PBC_RequestFeedbackLoopPIconsts.restype = c_bool
PBC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def request_feedback_loop_p_iconsts(serial_number):
    '''
    Requests that the feedback loop constants be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestFeedbackLoopPIconsts(serial_number)

    return output


PBC_RequestMaxOutputVoltage = lib.PBC_RequestMaxOutputVoltage
PBC_RequestMaxOutputVoltage.restype = c_bool
PBC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]


def request_max_output_voltage(serial_number):
    '''
    Requests that the maximum output voltage be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestMaxOutputVoltage(serial_number)

    return output


PBC_RequestMaximumTravel = lib.PBC_RequestMaximumTravel
PBC_RequestMaximumTravel.restype = c_bool
PBC_RequestMaximumTravel.argtypes = [POINTER(c_char)]


def request_maximum_travel(serial_number):
    '''
    Requests the maximum travel be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestMaximumTravel(serial_number)

    return output


PBC_RequestOutputVoltage = lib.PBC_RequestOutputVoltage
PBC_RequestOutputVoltage.restype = c_bool
PBC_RequestOutputVoltage.argtypes = [POINTER(c_char)]


def request_output_voltage(serial_number):
    '''
    Requests the output voltage be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestOutputVoltage(serial_number)

    return output


PBC_RequestPosition = lib.PBC_RequestPosition
PBC_RequestPosition.restype = c_short
PBC_RequestPosition.argtypes = [POINTER(c_char)]


def request_position(serial_number):
    '''
    Requests the current output voltage or position depending on current mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestPosition(serial_number)

    return output


PBC_RequestPositionControlMode = lib.PBC_RequestPositionControlMode
PBC_RequestPositionControlMode.restype = c_bool
PBC_RequestPositionControlMode.argtypes = [POINTER(c_char)]


def request_position_control_mode(serial_number):
    '''
    Requests the Position Control Mode be read from the device for the device and channel.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestPositionControlMode(serial_number)

    return output


PBC_RequestRackDigitalOutputs = lib.PBC_RequestRackDigitalOutputs
PBC_RequestRackDigitalOutputs.restype = c_short
PBC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]


def request_rack_digital_outputs(serial_number):
    '''
    Requests the rack digital output bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PBC_RequestRackDigitalOutputs(serial_number)

    return output


PBC_RequestRackStatusBits = lib.PBC_RequestRackStatusBits
PBC_RequestRackStatusBits.restype = c_short
PBC_RequestRackStatusBits.argtypes = [POINTER(c_char)]


def request_rack_status_bits(serial_number):
    '''
    Requests the Rack status bits be downloaded.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PBC_RequestRackStatusBits(serial_number)

    return output


PBC_RequestSettings = lib.PBC_RequestSettings
PBC_RequestSettings.restype = c_short
PBC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    '''
    Requests that all settings are download from device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestSettings(serial_number)

    return output


PBC_RequestStatus = lib.PBC_RequestStatus
PBC_RequestStatus.restype = c_short
PBC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    '''
    Requests the status bits and position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestStatus(serial_number)

    return output


PBC_RequestStatusBits = lib.PBC_RequestStatusBits
PBC_RequestStatusBits.restype = c_short
PBC_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits(serial_number):
    '''
    Request the status bits which identify the current device state.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestStatusBits(serial_number)

    return output


PBC_RequestVoltageSource = lib.PBC_RequestVoltageSource
PBC_RequestVoltageSource.restype = c_bool
PBC_RequestVoltageSource.argtypes = [POINTER(c_char)]


def request_voltage_source(serial_number):
    '''
    Requests that the current input voltage source be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_RequestVoltageSource(serial_number)

    return output


PBC_ResetParameters = lib.PBC_ResetParameters
PBC_ResetParameters.restype = c_short
PBC_ResetParameters.argtypes = [POINTER(c_char)]


def reset_parameters(serial_number):
    '''
    Resets all parameters to power-up values.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_ResetParameters(serial_number)

    return output


PBC_SetFeedbackLoopPIconsts = lib.PBC_SetFeedbackLoopPIconsts
PBC_SetFeedbackLoopPIconsts.restype = c_short
PBC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def set_feedback_loop_p_iconsts(serial_number):
    '''
    Sets the feedback loop constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        proportionalTerm: c_short
        integralTerm: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = PBC_SetFeedbackLoopPIconsts(serial_number)

    return output


PBC_SetFeedbackLoopPIconstsBlock = lib.PBC_SetFeedbackLoopPIconstsBlock
PBC_SetFeedbackLoopPIconstsBlock.restype = c_short
PBC_SetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


def set_feedback_loop_p_iconsts_block(serial_number):
    '''
    Sets the feedback loop constants in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        proportionalAndIntegralConstants: PZ_FeedbackLoopConstants

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PBC_SetFeedbackLoopPIconstsBlock(serial_number)

    return output


PBC_SetLUTwaveParams = lib.PBC_SetLUTwaveParams
PBC_SetLUTwaveParams.restype = c_short
PBC_SetLUTwaveParams.argtypes = [POINTER(c_char)]


def set_l_u_twave_params(serial_number):
    '''
    Sets the LUT output wave parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        LUTwaveParams: PZ_LUTWaveParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    LUTwaveParams = PZ_LUTWaveParameters()

    output = PBC_SetLUTwaveParams(serial_number)

    return output


PBC_SetLUTwaveSample = lib.PBC_SetLUTwaveSample
PBC_SetLUTwaveSample.restype = c_short
PBC_SetLUTwaveSample.argtypes = [POINTER(c_char)]


def set_l_u_twave_sample(serial_number):
    '''
    Sets a waveform sample.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        index: c_short
        value: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    index = c_short()
    value = c_long()

    output = PBC_SetLUTwaveSample(serial_number)

    return output


PBC_SetMaxOutputVoltage = lib.PBC_SetMaxOutputVoltage
PBC_SetMaxOutputVoltage.restype = c_short
PBC_SetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def set_max_output_voltage(serial_number):
    '''
    Sets the maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        maxVoltage: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    maxVoltage = c_short()

    output = PBC_SetMaxOutputVoltage(serial_number)

    return output


PBC_SetOutputVoltage = lib.PBC_SetOutputVoltage
PBC_SetOutputVoltage.restype = c_short
PBC_SetOutputVoltage.argtypes = [POINTER(c_char)]


def set_output_voltage(serial_number):
    '''
    Sets the output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        volts: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    volts = c_short()

    output = PBC_SetOutputVoltage(serial_number)

    return output


PBC_SetPosition = lib.PBC_SetPosition
PBC_SetPosition.restype = c_short
PBC_SetPosition.argtypes = [POINTER(c_char)]


def set_position(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        position: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    position = c_short()

    output = PBC_SetPosition(serial_number)

    return output


PBC_SetPositionControlMode = lib.PBC_SetPositionControlMode
PBC_SetPositionControlMode.restype = c_short
PBC_SetPositionControlMode.argtypes = [POINTER(c_char)]


def set_position_control_mode(serial_number):
    '''
    Sets the Position Control Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        mode: PZ_ControlModeTypes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    mode = PZ_ControlModeTypes()

    output = PBC_SetPositionControlMode(serial_number)

    return output


PBC_SetPositionToTolerance = lib.PBC_SetPositionToTolerance
PBC_SetPositionToTolerance.restype = c_short
PBC_SetPositionToTolerance.argtypes = [POINTER(c_char)]


def set_position_to_tolerance(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        position: c_short
        tolerance: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    position = c_short()
    tolerance = c_short()

    output = PBC_SetPositionToTolerance(serial_number)

    return output


PBC_SetRackDigitalOutputs = lib.PBC_SetRackDigitalOutputs
PBC_SetRackDigitalOutputs.restype = c_short
PBC_SetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def set_rack_digital_outputs(serial_number):
    '''
    Sets the rack digital output bits.

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

    output = PBC_SetRackDigitalOutputs(serial_number)

    return output


PBC_SetVoltageSource = lib.PBC_SetVoltageSource
PBC_SetVoltageSource.restype = c_short
PBC_SetVoltageSource.argtypes = [POINTER(c_char)]


def set_voltage_source(serial_number):
    '''
    Sets the control voltage source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        source: PZ_InputSourceFlags

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    source = PZ_InputSourceFlags()

    output = PBC_SetVoltageSource(serial_number)

    return output


PBC_SetZero = lib.PBC_SetZero
PBC_SetZero.restype = c_short
PBC_SetZero.argtypes = [POINTER(c_char)]


def set_zero(serial_number):
    '''
    Sets the voltage output to zero and defines the ensuing actuator position az zero.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_SetZero(serial_number)

    return output


PBC_StartLUTwave = lib.PBC_StartLUTwave
PBC_StartLUTwave.restype = c_short
PBC_StartLUTwave.argtypes = [POINTER(c_char)]


def start_l_u_twave(serial_number):
    '''
    Starts the LUT waveform output.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_StartLUTwave(serial_number)

    return output


PBC_StartPolling = lib.PBC_StartPolling
PBC_StartPolling.restype = c_bool
PBC_StartPolling.argtypes = [POINTER(c_char)]


def start_polling(serial_number):
    '''
    Starts the internal polling loop which continuously requests position and status.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        milliseconds: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    milliseconds = c_int()

    output = PBC_StartPolling(serial_number)

    return output


PBC_StopLUTwave = lib.PBC_StopLUTwave
PBC_StopLUTwave.restype = c_short
PBC_StopLUTwave.argtypes = [POINTER(c_char)]


def stop_l_u_twave(serial_number):
    '''
    Stops the LUT waveform output.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_StopLUTwave(serial_number)

    return output


PBC_StopPolling = lib.PBC_StopPolling
PBC_StopPolling.restype = c_void_p
PBC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    '''
    Stops the internal polling loop.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()

    output = PBC_StopPolling(serial_number)

    return output


PBC_TimeSinceLastMsgReceived = lib.PBC_TimeSinceLastMsgReceived
PBC_TimeSinceLastMsgReceived.restype = c_bool
PBC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


def time_since_last_msg_received(serial_number):
    '''
    Gets the time in milliseconds since tha last message was received from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        lastUpdateTimeMS: c_int64

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    lastUpdateTimeMS = c_int64()

    output = PBC_TimeSinceLastMsgReceived(serial_number)

    return output


PBC_WaitForMessage = lib.PBC_WaitForMessage
PBC_WaitForMessage.restype = c_bool
PBC_WaitForMessage.argtypes = [POINTER(c_char)]


def wait_for_message(serial_number):
    '''
    Get the next MessageQueue item if it is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_short
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PBC_WaitForMessage(serial_number)

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



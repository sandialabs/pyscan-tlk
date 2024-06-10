from ctypes import (POINTER, c_bool, c_byte, c_char, c_int, c_int32, c_int64, c_long, c_short, c_ulong, c_void_p, cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (PZ_ControlModeTypes, PZ_InputSourceFlags)
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
    # Check connection.

    serial_number = POINTER(c_char)

    output = PBC_CheckConnection(serial_number)

    return output


PBC_ClearMessageQueue = lib.PBC_ClearMessageQueue
PBC_ClearMessageQueue.restype = c_short
PBC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]


def clear_message_queue(serial_number, channel):
    # Clears the device message queue.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_ClearMessageQueue(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_Close = lib.PBC_Close
PBC_Close.restype = c_void_p
PBC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = PBC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_DisableChannel = lib.PBC_DisableChannel
PBC_DisableChannel.restype = c_short
PBC_DisableChannel.argtypes = [POINTER(c_char), c_short]


def disable_channel(serial_number, channel):
    # Disable the channel so that motor can be moved by hand.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_DisableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_Disconnect = lib.PBC_Disconnect
PBC_Disconnect.restype = c_short
PBC_Disconnect.argtypes = [POINTER(c_char)]


def disconnect(serial_number):
    # Tells the device that it is being disconnected.

    serial_number = POINTER(c_char)

    output = PBC_Disconnect(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_EnableChannel = lib.PBC_EnableChannel
PBC_EnableChannel.restype = c_short
PBC_EnableChannel.argtypes = [POINTER(c_char), c_short]


def enable_channel(serial_number, channel):
    # Enable channel for computer control.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_EnableChannel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_EnableLastMsgTimer = lib.PBC_EnableLastMsgTimer
PBC_EnableLastMsgTimer.restype = c_void_p
PBC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]


def enable_last_msg_timer(serial_number, channel):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    channel = c_short()
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = PBC_EnableLastMsgTimer(serial_number, channel, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


PBC_GetFeedbackLoopPIconsts = lib.PBC_GetFeedbackLoopPIconsts
PBC_GetFeedbackLoopPIconsts.restype = c_short
PBC_GetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short, c_short]


def get_feedback_loop_p_iconsts(serial_number, channel):
    # Gets the feedback loop parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = PBC_GetFeedbackLoopPIconsts(serial_number, channel, proportionalTerm, integralTerm)
    if output != 0:
        raise KinesisException(output)


PBC_GetFeedbackLoopPIconstsBlock = lib.PBC_GetFeedbackLoopPIconstsBlock
PBC_GetFeedbackLoopPIconstsBlock.restype = c_short
PBC_GetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char), c_short, PZ_FeedbackLoopConstants]


def get_feedback_loop_p_iconsts_block(serial_number, channel):
    # Gets the feedback loop constants in a block.

    serial_number = POINTER(c_char)
    channel = c_short()
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PBC_GetFeedbackLoopPIconstsBlock(serial_number, channel, proportionalAndIntegralConstants)
    if output != 0:
        raise KinesisException(output)


PBC_GetFirmwareVersion = lib.PBC_GetFirmwareVersion
PBC_GetFirmwareVersion.restype = c_ulong
PBC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of the device firmware.

    serial_number = POINTER(c_char)

    output = PBC_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_GetHardwareInfo = lib.PBC_GetHardwareInfo
PBC_GetHardwareInfo.restype = c_short
PBC_GetHardwareInfo.argtypes = [
    POINTER(c_char),
    c_short,
    POINTER(c_char),
    c_ulong,
    c_long,
    c_long,
    POINTER(c_char),
    c_ulong,
    c_ulong,
    c_long,
    c_long]


def get_hardware_info(serial_number, channel):
    # Gets the hardware information from the device.

    serial_number = POINTER(c_char)
    channel = c_short()
    modelNo = POINTER(c_char)
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = PBC_GetHardwareInfo(
        serial_number,
        channel,
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


PBC_GetHardwareInfoBlock = lib.PBC_GetHardwareInfoBlock
PBC_GetHardwareInfoBlock.restype = c_short
PBC_GetHardwareInfoBlock.argtypes = [POINTER(c_char), c_short, TLI_HardwareInformation]


def get_hardware_info_block(serial_number, channel):
    # Gets the hardware information in a block.

    serial_number = POINTER(c_char)
    channel = c_short()
    hardwareInfo = TLI_HardwareInformation()

    output = PBC_GetHardwareInfoBlock(serial_number, channel, hardwareInfo)
    if output != 0:
        raise KinesisException(output)


PBC_GetMaxOutputVoltage = lib.PBC_GetMaxOutputVoltage
PBC_GetMaxOutputVoltage.restype = c_short
PBC_GetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]


def get_max_output_voltage(serial_number, channel):
    # Gets the maximum output voltage.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_GetMaxOutputVoltage(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_GetMaximumTravel = lib.PBC_GetMaximumTravel
PBC_GetMaximumTravel.restype = c_long
PBC_GetMaximumTravel.argtypes = [POINTER(c_char), c_short]


def get_maximum_travel(serial_number, channel):
    # Gets the maximum travel of the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_GetMaximumTravel(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_GetNextMessage = lib.PBC_GetNextMessage
PBC_GetNextMessage.restype = c_bool
PBC_GetNextMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


def get_next_message(serial_number, channel):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PBC_GetNextMessage(serial_number, channel, messageType, messageID, messageData)

    return output


PBC_GetNumChannels = lib.PBC_GetNumChannels
PBC_GetNumChannels.restype = c_short
PBC_GetNumChannels.argtypes = [POINTER(c_char)]


def get_num_channels(serial_number):
    # Gets the number of channels in the device.

    serial_number = POINTER(c_char)

    output = PBC_GetNumChannels(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_GetOutputVoltage = lib.PBC_GetOutputVoltage
PBC_GetOutputVoltage.restype = c_short
PBC_GetOutputVoltage.argtypes = [POINTER(c_char), c_short]


def get_output_voltage(serial_number, channel):
    # Gets the set Output Voltage.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_GetOutputVoltage(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_GetPosition = lib.PBC_GetPosition
PBC_GetPosition.restype = c_short
PBC_GetPosition.argtypes = [POINTER(c_char), c_short]


def get_position(serial_number, channel):
    # Gets the position when in closed loop mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_GetPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_GetPositionControlMode = lib.PBC_GetPositionControlMode
PBC_GetPositionControlMode.restype = PZ_ControlModeTypes
PBC_GetPositionControlMode.argtypes = [POINTER(c_char), c_short]


def get_position_control_mode(serial_number, channel):
    # Gets the Position Control Mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_GetPositionControlMode(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_GetRackDigitalOutputs = lib.PBC_GetRackDigitalOutputs
PBC_GetRackDigitalOutputs.restype = c_byte
PBC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def get_rack_digital_outputs(serial_number):
    # Gets the rack digital output bits.

    serial_number = POINTER(c_char)

    output = PBC_GetRackDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_GetRackStatusBits = lib.PBC_GetRackStatusBits
PBC_GetRackStatusBits.restype = c_ulong
PBC_GetRackStatusBits.argtypes = [POINTER(c_char)]


def get_rack_status_bits(serial_number):
    # Gets the Rack status bits.

    serial_number = POINTER(c_char)

    output = PBC_GetRackStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_GetSoftwareVersion = lib.PBC_GetSoftwareVersion
PBC_GetSoftwareVersion.restype = c_ulong
PBC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = PBC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_GetStatusBits = lib.PBC_GetStatusBits
PBC_GetStatusBits.restype = c_ulong
PBC_GetStatusBits.argtypes = [POINTER(c_char), c_short]


def get_status_bits(serial_number, channel):
    # Get the current status bits.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_GetStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_GetVoltageSource = lib.PBC_GetVoltageSource
PBC_GetVoltageSource.restype = PZ_InputSourceFlags
PBC_GetVoltageSource.argtypes = [POINTER(c_char), c_short]


def get_voltage_source(serial_number, channel):
    # Gets the control voltage source.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_GetVoltageSource(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_HasLastMsgTimerOverrun = lib.PBC_HasLastMsgTimerOverrun
PBC_HasLastMsgTimerOverrun.restype = c_bool
PBC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]


def has_last_msg_timer_overrun(serial_number, channel):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by PBC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_HasLastMsgTimerOverrun(serial_number, channel)

    return output


PBC_Identify = lib.PBC_Identify
PBC_Identify.restype = c_void_p
PBC_Identify.argtypes = [POINTER(c_char), c_short]


def identify(serial_number, channel):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_Identify(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_IsChannelValid = lib.PBC_IsChannelValid
PBC_IsChannelValid.restype = c_bool
PBC_IsChannelValid.argtypes = [POINTER(c_char), c_short]


def is_channel_valid(serial_number, channel):
    # Verifies that the specified channel is valid.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_IsChannelValid(serial_number, channel)

    return output


PBC_LoadNamedSettings = lib.PBC_LoadNamedSettings
PBC_LoadNamedSettings.restype = c_bool
PBC_LoadNamedSettings.argtypes = [POINTER(c_char), c_short, POINTER(c_char)]


def load_named_settings(serial_number, channel):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    channel = c_short()
    settingsName = POINTER(c_char)

    output = PBC_LoadNamedSettings(serial_number, channel, settingsName)

    return output


PBC_LoadSettings = lib.PBC_LoadSettings
PBC_LoadSettings.restype = c_bool
PBC_LoadSettings.argtypes = [POINTER(c_char), c_short]


def load_settings(serial_number, channel):
    # Update device with stored settings.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_LoadSettings(serial_number, channel)

    return output


PBC_MaxChannelCount = lib.PBC_MaxChannelCount
PBC_MaxChannelCount.restype = c_int
PBC_MaxChannelCount.argtypes = [POINTER(c_char)]


def max_channel_count(serial_number):
    # Gets the number of channels available to this device.

    serial_number = POINTER(c_char)

    output = PBC_MaxChannelCount(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_MessageQueueSize = lib.PBC_MessageQueueSize
PBC_MessageQueueSize.restype = c_int
PBC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]


def message_queue_size(serial_number, channel):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_MessageQueueSize(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_Open = lib.PBC_Open
PBC_Open.restype = c_short
PBC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = PBC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_PersistSettings = lib.PBC_PersistSettings
PBC_PersistSettings.restype = c_bool
PBC_PersistSettings.argtypes = [POINTER(c_char), c_short]


def persist_settings(serial_number, channel):
    # Persist device settings to device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_PersistSettings(serial_number, channel)

    return output


PBC_PollingDuration = lib.PBC_PollingDuration
PBC_PollingDuration.restype = c_long
PBC_PollingDuration.argtypes = [POINTER(c_char), c_short]


def polling_duration(serial_number, channel):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_PollingDuration(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_RegisterMessageCallback = lib.PBC_RegisterMessageCallback
PBC_RegisterMessageCallback.restype = c_short
PBC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, c_void_p]


def register_message_callback(serial_number, channel):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    channel = c_short()
    void = c_void_p()

    output = PBC_RegisterMessageCallback(serial_number, channel, void)
    if output != 0:
        raise KinesisException(output)


PBC_RequestActualPosition = lib.PBC_RequestActualPosition
PBC_RequestActualPosition.restype = c_short
PBC_RequestActualPosition.argtypes = [POINTER(c_char), c_short]


def request_actual_position(serial_number, channel):
    # Requests the position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestActualPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_RequestFeedbackLoopPIconsts = lib.PBC_RequestFeedbackLoopPIconsts
PBC_RequestFeedbackLoopPIconsts.restype = c_bool
PBC_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short]


def request_feedback_loop_p_iconsts(serial_number, channel):
    # Requests that the feedback loop constants be read from the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestFeedbackLoopPIconsts(serial_number, channel)

    return output


PBC_RequestMaxOutputVoltage = lib.PBC_RequestMaxOutputVoltage
PBC_RequestMaxOutputVoltage.restype = c_bool
PBC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char), c_short]


def request_max_output_voltage(serial_number, channel):
    # Requests that the maximum output voltage be read from the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestMaxOutputVoltage(serial_number, channel)

    return output


PBC_RequestMaximumTravel = lib.PBC_RequestMaximumTravel
PBC_RequestMaximumTravel.restype = c_bool
PBC_RequestMaximumTravel.argtypes = [POINTER(c_char), c_short]


def request_maximum_travel(serial_number, channel):
    # Requests the maximum travel be read from the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestMaximumTravel(serial_number, channel)

    return output


PBC_RequestOutputVoltage = lib.PBC_RequestOutputVoltage
PBC_RequestOutputVoltage.restype = c_bool
PBC_RequestOutputVoltage.argtypes = [POINTER(c_char), c_short]


def request_output_voltage(serial_number, channel):
    # Requests the output voltage be read from the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestOutputVoltage(serial_number, channel)

    return output


PBC_RequestPosition = lib.PBC_RequestPosition
PBC_RequestPosition.restype = c_short
PBC_RequestPosition.argtypes = [POINTER(c_char), c_short]


def request_position(serial_number, channel):
    # Requests the current output voltage or position depending on current mode.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestPosition(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_RequestPositionControlMode = lib.PBC_RequestPositionControlMode
PBC_RequestPositionControlMode.restype = c_bool
PBC_RequestPositionControlMode.argtypes = [POINTER(c_char), c_short]


def request_position_control_mode(serial_number, channel):
    # Requests the Position Control Mode be read from the device for the device and channel.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestPositionControlMode(serial_number, channel)

    return output


PBC_RequestRackDigitalOutputs = lib.PBC_RequestRackDigitalOutputs
PBC_RequestRackDigitalOutputs.restype = c_short
PBC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]


def request_rack_digital_outputs(serial_number):
    # Requests the rack digital output bits.

    serial_number = POINTER(c_char)

    output = PBC_RequestRackDigitalOutputs(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_RequestRackStatusBits = lib.PBC_RequestRackStatusBits
PBC_RequestRackStatusBits.restype = c_short
PBC_RequestRackStatusBits.argtypes = [POINTER(c_char)]


def request_rack_status_bits(serial_number):
    # Requests the Rack status bits be downloaded.

    serial_number = POINTER(c_char)

    output = PBC_RequestRackStatusBits(serial_number)
    if output != 0:
        raise KinesisException(output)


PBC_RequestSettings = lib.PBC_RequestSettings
PBC_RequestSettings.restype = c_short
PBC_RequestSettings.argtypes = [POINTER(c_char), c_short]


def request_settings(serial_number, channel):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestSettings(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_RequestStatus = lib.PBC_RequestStatus
PBC_RequestStatus.restype = c_short
PBC_RequestStatus.argtypes = [POINTER(c_char), c_short]


def request_status(serial_number, channel):
    # Requests the status bits and position.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestStatus(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_RequestStatusBits = lib.PBC_RequestStatusBits
PBC_RequestStatusBits.restype = c_short
PBC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]


def request_status_bits(serial_number, channel):
    # Request the status bits which identify the current device state.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestStatusBits(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_RequestVoltageSource = lib.PBC_RequestVoltageSource
PBC_RequestVoltageSource.restype = c_bool
PBC_RequestVoltageSource.argtypes = [POINTER(c_char), c_short]


def request_voltage_source(serial_number, channel):
    # Requests that the current input voltage source be read from the device.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_RequestVoltageSource(serial_number, channel)

    return output


PBC_ResetParameters = lib.PBC_ResetParameters
PBC_ResetParameters.restype = c_short
PBC_ResetParameters.argtypes = [POINTER(c_char), c_short]


def reset_parameters(serial_number, channel):
    # Resets all parameters to power-up values.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_ResetParameters(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_SetFeedbackLoopPIconsts = lib.PBC_SetFeedbackLoopPIconsts
PBC_SetFeedbackLoopPIconsts.restype = c_short
PBC_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char), c_short, c_short, c_short]


def set_feedback_loop_p_iconsts(serial_number, channel):
    # Sets the feedback loop constants.

    serial_number = POINTER(c_char)
    channel = c_short()
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = PBC_SetFeedbackLoopPIconsts(serial_number, channel, proportionalTerm, integralTerm)
    if output != 0:
        raise KinesisException(output)


PBC_SetFeedbackLoopPIconstsBlock = lib.PBC_SetFeedbackLoopPIconstsBlock
PBC_SetFeedbackLoopPIconstsBlock.restype = c_short
PBC_SetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char), c_short, PZ_FeedbackLoopConstants]


def set_feedback_loop_p_iconsts_block(serial_number, channel):
    # Sets the feedback loop constants in a block.

    serial_number = POINTER(c_char)
    channel = c_short()
    proportionalAndIntegralConstants = PZ_FeedbackLoopConstants()

    output = PBC_SetFeedbackLoopPIconstsBlock(serial_number, channel, proportionalAndIntegralConstants)
    if output != 0:
        raise KinesisException(output)


PBC_SetLUTwaveParams = lib.PBC_SetLUTwaveParams
PBC_SetLUTwaveParams.restype = c_short
PBC_SetLUTwaveParams.argtypes = [POINTER(c_char), c_short, PZ_LUTWaveParameters]


def set_l_u_twave_params(serial_number, channel):
    # Sets the LUT output wave parameters.

    serial_number = POINTER(c_char)
    channel = c_short()
    LUTwaveParams = PZ_LUTWaveParameters()

    output = PBC_SetLUTwaveParams(serial_number, channel, LUTwaveParams)
    if output != 0:
        raise KinesisException(output)


PBC_SetLUTwaveSample = lib.PBC_SetLUTwaveSample
PBC_SetLUTwaveSample.restype = c_short
PBC_SetLUTwaveSample.argtypes = [POINTER(c_char), c_short, c_short, c_long]


def set_l_u_twave_sample(serial_number, channel):
    # Sets a waveform sample.

    serial_number = POINTER(c_char)
    channel = c_short()
    index = c_short()
    value = c_long()

    output = PBC_SetLUTwaveSample(serial_number, channel, index, value)
    if output != 0:
        raise KinesisException(output)


PBC_SetMaxOutputVoltage = lib.PBC_SetMaxOutputVoltage
PBC_SetMaxOutputVoltage.restype = c_short
PBC_SetMaxOutputVoltage.argtypes = [POINTER(c_char), c_short, c_short]


def set_max_output_voltage(serial_number, channel):
    # Sets the maximum output voltage.

    serial_number = POINTER(c_char)
    channel = c_short()
    maxVoltage = c_short()

    output = PBC_SetMaxOutputVoltage(serial_number, channel, maxVoltage)
    if output != 0:
        raise KinesisException(output)


PBC_SetOutputVoltage = lib.PBC_SetOutputVoltage
PBC_SetOutputVoltage.restype = c_short
PBC_SetOutputVoltage.argtypes = [POINTER(c_char), c_short, c_short]


def set_output_voltage(serial_number, channel):
    # Sets the output voltage.

    serial_number = POINTER(c_char)
    channel = c_short()
    volts = c_short()

    output = PBC_SetOutputVoltage(serial_number, channel, volts)
    if output != 0:
        raise KinesisException(output)


PBC_SetPosition = lib.PBC_SetPosition
PBC_SetPosition.restype = c_short
PBC_SetPosition.argtypes = [POINTER(c_char), c_short, c_short]


def set_position(serial_number, channel):
    # Sets the position when in closed loop mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    position = c_short()

    output = PBC_SetPosition(serial_number, channel, position)
    if output != 0:
        raise KinesisException(output)


PBC_SetPositionControlMode = lib.PBC_SetPositionControlMode
PBC_SetPositionControlMode.restype = c_short
PBC_SetPositionControlMode.argtypes = [POINTER(c_char), c_short, PZ_ControlModeTypes]


def set_position_control_mode(serial_number, channel):
    # Sets the Position Control Mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    mode = PZ_ControlModeTypes()

    output = PBC_SetPositionControlMode(serial_number, channel, mode)
    if output != 0:
        raise KinesisException(output)


PBC_SetPositionToTolerance = lib.PBC_SetPositionToTolerance
PBC_SetPositionToTolerance.restype = c_short
PBC_SetPositionToTolerance.argtypes = [POINTER(c_char), c_short, c_short, c_short]


def set_position_to_tolerance(serial_number, channel):
    # Sets the position when in closed loop mode.

    serial_number = POINTER(c_char)
    channel = c_short()
    position = c_short()
    tolerance = c_short()

    output = PBC_SetPositionToTolerance(serial_number, channel, position, tolerance)
    if output != 0:
        raise KinesisException(output)


PBC_SetRackDigitalOutputs = lib.PBC_SetRackDigitalOutputs
PBC_SetRackDigitalOutputs.restype = c_short
PBC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]


def set_rack_digital_outputs(serial_number):
    # Sets the rack digital output bits.

    serial_number = POINTER(c_char)
    outputsBits = c_byte()

    output = PBC_SetRackDigitalOutputs(serial_number, outputsBits)
    if output != 0:
        raise KinesisException(output)


PBC_SetVoltageSource = lib.PBC_SetVoltageSource
PBC_SetVoltageSource.restype = c_short
PBC_SetVoltageSource.argtypes = [POINTER(c_char), c_short, PZ_InputSourceFlags]


def set_voltage_source(serial_number, channel):
    # Sets the control voltage source.

    serial_number = POINTER(c_char)
    channel = c_short()
    source = PZ_InputSourceFlags()

    output = PBC_SetVoltageSource(serial_number, channel, source)
    if output != 0:
        raise KinesisException(output)


PBC_SetZero = lib.PBC_SetZero
PBC_SetZero.restype = c_short
PBC_SetZero.argtypes = [POINTER(c_char), c_short]


def set_zero(serial_number, channel):
    # Sets the voltage output to zero and defines the ensuing actuator position az zero.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_SetZero(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_StartLUTwave = lib.PBC_StartLUTwave
PBC_StartLUTwave.restype = c_short
PBC_StartLUTwave.argtypes = [POINTER(c_char), c_short]


def start_l_u_twave(serial_number, channel):
    # Starts the LUT waveform output.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_StartLUTwave(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_StartPolling = lib.PBC_StartPolling
PBC_StartPolling.restype = c_bool
PBC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]


def start_polling(serial_number, channel):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    channel = c_short()
    milliseconds = c_int()

    output = PBC_StartPolling(serial_number, channel, milliseconds)

    return output


PBC_StopLUTwave = lib.PBC_StopLUTwave
PBC_StopLUTwave.restype = c_short
PBC_StopLUTwave.argtypes = [POINTER(c_char), c_short]


def stop_l_u_twave(serial_number, channel):
    # Stops the LUT waveform output.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_StopLUTwave(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_StopPolling = lib.PBC_StopPolling
PBC_StopPolling.restype = c_void_p
PBC_StopPolling.argtypes = [POINTER(c_char), c_short]


def stop_polling(serial_number, channel):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)
    channel = c_short()

    output = PBC_StopPolling(serial_number, channel)
    if output != 0:
        raise KinesisException(output)


PBC_TimeSinceLastMsgReceived = lib.PBC_TimeSinceLastMsgReceived
PBC_TimeSinceLastMsgReceived.restype = c_bool
PBC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_short, c_int64]


def time_since_last_msg_received(serial_number, channel):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    channel = c_short()
    lastUpdateTimeMS = c_int64()

    output = PBC_TimeSinceLastMsgReceived(serial_number, channel, lastUpdateTimeMS)

    return output


PBC_WaitForMessage = lib.PBC_WaitForMessage
PBC_WaitForMessage.restype = c_bool
PBC_WaitForMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


def wait_for_message(serial_number, channel):
    # Get the next MessageQueue item if it is available.

    serial_number = POINTER(c_char)
    channel = c_short()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PBC_WaitForMessage(serial_number, channel, messageType, messageID, messageData)

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

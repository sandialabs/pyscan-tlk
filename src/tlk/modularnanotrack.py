from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_char_p,
    c_double,
    c_float,
    c_int,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
from .definitions.enumerations import (
    KNA_FeedbackSource,
    KNA_TIARange,
    NT_ControlMode,
    NT_FeedbackSource,
    NT_Mode,
    NT_OddOrEven,
    NT_TIARange,
    NT_TIARangeMode)
from .definitions.structures import (
    KNA_TIARangeParameters,
    KNA_TIAReading,
    NT_CircleDiameterLUT,
    NT_CircleParameters,
    NT_HVComponent,
    NT_LowPassFilterParameters,
    NT_TIARangeParameters,
    NT_TIAReading,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Modular.DLL")

NT_ChannelEnable = lib.NT_ChannelEnable
NT_ChannelEnable.restype = c_short
NT_ChannelEnable.argtypes = [POINTER(c_char)]


def channel_enable(serial_number):
    '''
    Enable / Disable the specified channel.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_long
        enable: c_bool

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_long()
    enable = c_bool()

    output = NT_ChannelEnable(serial_number)

    return output


NT_CheckConnection = lib.NT_CheckConnection
NT_CheckConnection.restype = c_bool
NT_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = NT_CheckConnection(serial_number)

    return output


NT_ClearMessageQueue = lib.NT_ClearMessageQueue
NT_ClearMessageQueue.restype = c_void_p
NT_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    '''
    clears the message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_ClearMessageQueue(serial_number)

    return output


NT_Close = lib.NT_Close
NT_Close.restype = c_void_p
NT_Close.argtypes = [POINTER(c_char)]


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

    output = NT_Close(serial_number)

    return output


NT_Disconnect = lib.NT_Disconnect
NT_Disconnect.restype = c_short
NT_Disconnect.argtypes = [POINTER(c_char)]


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

    output = NT_Disconnect(serial_number)

    return output


NT_EnableLastMsgTimer = lib.NT_EnableLastMsgTimer
NT_EnableLastMsgTimer.restype = c_void_p
NT_EnableLastMsgTimer.argtypes = [POINTER(c_char)]


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

    output = NT_EnableLastMsgTimer(serial_number)

    return output


NT_GetCircleDiameter = lib.NT_GetCircleDiameter
NT_GetCircleDiameter.restype = c_long
NT_GetCircleDiameter.argtypes = [POINTER(c_char)]


def get_circle_diameter(serial_number):
    '''
    Gets the scan circle diameter.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetCircleDiameter(serial_number)

    return output


NT_GetCircleDiameterLUT = lib.NT_GetCircleDiameterLUT
NT_GetCircleDiameterLUT.restype = c_short
NT_GetCircleDiameterLUT.argtypes = [POINTER(c_char)]


def get_circle_diameter_l_u_t(serial_number):
    '''
    Gets the scan circle diameter Lookup Table (LUT).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        LUT: NT_CircleDiameterLUT

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    LUT = NT_CircleDiameterLUT()

    output = NT_GetCircleDiameterLUT(serial_number)

    return output


NT_GetCircleHomePosition = lib.NT_GetCircleHomePosition
NT_GetCircleHomePosition.restype = c_short
NT_GetCircleHomePosition.argtypes = [POINTER(c_char)]


def get_circle_home_position(serial_number):
    '''
    Gets the home position of the scan circle.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: NT_HVComponent

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = NT_HVComponent()

    output = NT_GetCircleHomePosition(serial_number)

    return output


NT_GetCircleParams = lib.NT_GetCircleParams
NT_GetCircleParams.restype = c_short
NT_GetCircleParams.argtypes = [POINTER(c_char)]


def get_circle_params(serial_number):
    '''
    Gets the scanning circle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_CircleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_CircleParameters()

    output = NT_GetCircleParams(serial_number)

    return output


NT_GetCirclePosition = lib.NT_GetCirclePosition
NT_GetCirclePosition.restype = c_short
NT_GetCirclePosition.argtypes = [POINTER(c_char)]


def get_circle_position(serial_number):
    '''
    Gets the current scan circle centre position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: NT_HVComponent

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = NT_HVComponent()

    output = NT_GetCirclePosition(serial_number)

    return output


NT_GetControlMode = lib.NT_GetControlMode
NT_GetControlMode.restype = NT_ControlMode
NT_GetControlMode.argtypes = [POINTER(c_char)]


def get_control_mode(serial_number):
    '''
    Get the NanoTrak control mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_long

    Returns
    -------
        NT_ControlMode
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_long()

    output = NT_GetControlMode(serial_number)

    return output


NT_GetFeedbackSource = lib.NT_GetFeedbackSource
NT_GetFeedbackSource.restype = NT_FeedbackSource
NT_GetFeedbackSource.argtypes = [POINTER(c_char)]


def get_feedback_source(serial_number):
    '''
    Gets the NanoTrak feedback source.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        NT_FeedbackSource
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetFeedbackSource(serial_number)

    return output


NT_GetFirmwareVersion = lib.NT_GetFirmwareVersion
NT_GetFirmwareVersion.restype = c_ulong
NT_GetFirmwareVersion.argtypes = [POINTER(c_char)]


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

    output = NT_GetFirmwareVersion(serial_number)

    return output


NT_GetGain = lib.NT_GetGain
NT_GetGain.restype = c_short
NT_GetGain.argtypes = [POINTER(c_char)]


def get_gain(serial_number):
    '''
    Gets the control loop gain.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetGain(serial_number)

    return output


NT_GetHardwareInfo = lib.NT_GetHardwareInfo
NT_GetHardwareInfo.restype = c_short
NT_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = NT_GetHardwareInfo(serial_number)

    return output


NT_GetHardwareInfoBlock = lib.NT_GetHardwareInfoBlock
NT_GetHardwareInfoBlock.restype = c_short
NT_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = NT_GetHardwareInfoBlock(serial_number)

    return output


NT_GetMaxTravel = lib.NT_GetMaxTravel
NT_GetMaxTravel.restype = c_short
NT_GetMaxTravel.argtypes = [POINTER(c_char)]


def get_max_travel(serial_number):
    '''
    Gets the MaxTravel for the Piezos in um.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        chanA: c_double
        chanB: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    chanA = c_double()
    chanB = c_double()

    output = NT_GetMaxTravel(serial_number)

    return output


NT_GetMode = lib.NT_GetMode
NT_GetMode.restype = NT_Mode
NT_GetMode.argtypes = [POINTER(c_char)]


def get_mode(serial_number):
    '''
    Gets the nanoTrak operating mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        NT_Mode
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetMode(serial_number)

    return output


NT_GetNTChannels = lib.NT_GetNTChannels
NT_GetNTChannels.restype = c_short
NT_GetNTChannels.argtypes = [POINTER(c_char)]


def get_n_t_channels(serial_number):
    '''
    Gets the NanoTrak channels to (usually) piezos.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        chanA: c_short
        chanB: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    chanA = c_short()
    chanB = c_short()

    output = NT_GetNTChannels(serial_number)

    return output


NT_GetNextMessage = lib.NT_GetNextMessage
NT_GetNextMessage.restype = c_bool
NT_GetNextMessage.argtypes = [POINTER(c_char)]


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

    output = NT_GetNextMessage(serial_number)

    return output


NT_GetPhaseCompensationParams = lib.NT_GetPhaseCompensationParams
NT_GetPhaseCompensationParams.restype = c_short
NT_GetPhaseCompensationParams.argtypes = [POINTER(c_char)]


def get_phase_compensation_params(serial_number):
    '''
    Gets the phase compensation parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_HVComponent

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_HVComponent()

    output = NT_GetPhaseCompensationParams(serial_number)

    return output


NT_GetRangeMode = lib.NT_GetRangeMode
NT_GetRangeMode.restype = c_short
NT_GetRangeMode.argtypes = [POINTER(c_char)]


def get_range_mode(serial_number):
    '''
    Get the TIA Range Mode and OddEven mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: NT_TIARangeMode
        oddOrEven: NT_OddOrEven

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = NT_TIARangeMode()
    oddOrEven = NT_OddOrEven()

    output = NT_GetRangeMode(serial_number)

    return output


NT_GetReading = lib.NT_GetReading
NT_GetReading.restype = c_short
NT_GetReading.argtypes = [POINTER(c_char)]


def get_reading(serial_number):
    '''
    Gets a reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        reading: NT_TIAReading
        reading: KNA_TIAReading

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    reading = NT_TIAReading()
    reading = KNA_TIAReading()

    output = NT_GetReading(serial_number)

    return output


NT_GetSignalState = lib.NT_GetSignalState
NT_GetSignalState.restype = NT_SignalState
NT_GetSignalState.argtypes = [POINTER(c_char)]


def get_signal_state(serial_number):
    '''
    Gets the NanoTrak signal state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        NT_SignalState
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetSignalState(serial_number)

    return output


NT_GetSoftwareVersion = lib.NT_GetSoftwareVersion
NT_GetSoftwareVersion.restype = c_ulong
NT_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    output = NT_GetSoftwareVersion(serial_number)

    return output


NT_GetStatusBits = lib.NT_GetStatusBits
NT_GetStatusBits.restype = c_ulong
NT_GetStatusBits.argtypes = [POINTER(c_char)]


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

    output = NT_GetStatusBits(serial_number)

    return output


NT_GetTIALPFilterParams = lib.NT_GetTIALPFilterParams
NT_GetTIALPFilterParams.restype = c_short
NT_GetTIALPFilterParams.argtypes = [POINTER(c_char)]


def get_t_i_a_l_p_filter_params(serial_number):
    '''
    Gets the TIA long pass filter parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_LowPassFilterParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_LowPassFilterParameters()

    output = NT_GetTIALPFilterParams(serial_number)

    return output


NT_GetTIARange = lib.NT_GetTIARange
NT_GetTIARange.restype = NT_TIARange
NT_GetTIARange.argtypes = [POINTER(c_char)]


def get_t_i_a_range(serial_number):
    '''
    Gets the TIA range.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        NT_TIARange
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetTIARange(serial_number)

    return output


NT_GetTIArangeParams = lib.NT_GetTIArangeParams
NT_GetTIArangeParams.restype = c_short
NT_GetTIArangeParams.argtypes = [POINTER(c_char)]


def get_t_i_arange_params(serial_number):
    '''
    Gets the TIA range parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_TIARangeParameters
        params: KNA_TIARangeParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_TIARangeParameters()
    params = KNA_TIARangeParameters()

    output = NT_GetTIArangeParams(serial_number)

    return output


NT_GetTrackingThresholdSignal = lib.NT_GetTrackingThresholdSignal
NT_GetTrackingThresholdSignal.restype = c_float
NT_GetTrackingThresholdSignal.argtypes = [POINTER(c_char)]


def get_tracking_threshold_signal(serial_number):
    '''
    Gets the tracking threshold signal.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_float
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetTrackingThresholdSignal(serial_number)

    return output


NT_HasLastMsgTimerOverrun = lib.NT_HasLastMsgTimerOverrun
NT_HasLastMsgTimerOverrun.restype = c_bool
NT_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by NT_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_HasLastMsgTimerOverrun(serial_number)

    return output


NT_HomeCircle = lib.NT_HomeCircle
NT_HomeCircle.restype = c_short
NT_HomeCircle.argtypes = [POINTER(c_char)]


def home_circle(serial_number):
    '''
    Move the scan circle to the home position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_HomeCircle(serial_number)

    return output


NT_Identify = lib.NT_Identify
NT_Identify.restype = c_void_p
NT_Identify.argtypes = [POINTER(c_char)]


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

    output = NT_Identify(serial_number)

    return output


NT_IsChannelEnabled = lib.NT_IsChannelEnabled
NT_IsChannelEnabled.restype = c_bool
NT_IsChannelEnabled.argtypes = [POINTER(c_char)]


def is_channel_enabled(serial_number):
    '''
    Get the channel enabled state.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_long

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_long()

    output = NT_IsChannelEnabled(serial_number)

    return output


NT_LoadNamedSettings = lib.NT_LoadNamedSettings
NT_LoadNamedSettings.restype = c_bool
NT_LoadNamedSettings.argtypes = [POINTER(c_char)]


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

    output = NT_LoadNamedSettings(serial_number)

    return output


NT_LoadSettings = lib.NT_LoadSettings
NT_LoadSettings.restype = c_bool
NT_LoadSettings.argtypes = [POINTER(c_char)]


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

    output = NT_LoadSettings(serial_number)

    return output


NT_MessageQueueSize = lib.NT_MessageQueueSize
NT_MessageQueueSize.restype = c_int
NT_MessageQueueSize.argtypes = [POINTER(c_char)]


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

    output = NT_MessageQueueSize(serial_number)

    return output


NT_Open = lib.NT_Open
NT_Open.restype = c_short
NT_Open.argtypes = [POINTER(c_char)]


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

    output = NT_Open(serial_number)

    return output


NT_PollingDuration = lib.NT_PollingDuration
NT_PollingDuration.restype = c_long
NT_PollingDuration.argtypes = [POINTER(c_char)]


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

    output = NT_PollingDuration(serial_number)

    return output


NT_RegisterMessageCallback = lib.NT_RegisterMessageCallback
NT_RegisterMessageCallback.restype = c_void_p
NT_RegisterMessageCallback.argtypes = [POINTER(c_char)]


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

    output = NT_RegisterMessageCallback(serial_number)

    return output


NT_RequestChannelStates = lib.NT_RequestChannelStates
NT_RequestChannelStates.restype = c_short
NT_RequestChannelStates.argtypes = [POINTER(c_char)]


def request_channel_states(serial_number):
    '''
    Request the channel states from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestChannelStates(serial_number)

    return output


NT_RequestCircleDiameterLUT = lib.NT_RequestCircleDiameterLUT
NT_RequestCircleDiameterLUT.restype = c_short
NT_RequestCircleDiameterLUT.argtypes = [POINTER(c_char)]


def request_circle_diameter_l_u_t(serial_number):
    '''
    Requests the scan circle diameter Lookup Table (LUT).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestCircleDiameterLUT(serial_number)

    return output


NT_RequestCircleHomePosition = lib.NT_RequestCircleHomePosition
NT_RequestCircleHomePosition.restype = c_short
NT_RequestCircleHomePosition.argtypes = [POINTER(c_char)]


def request_circle_home_position(serial_number):
    '''
    Requests the home position of the scan circle.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestCircleHomePosition(serial_number)

    return output


NT_RequestCircleParams = lib.NT_RequestCircleParams
NT_RequestCircleParams.restype = c_short
NT_RequestCircleParams.argtypes = [POINTER(c_char)]


def request_circle_params(serial_number):
    '''
    Requests the scanning circle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestCircleParams(serial_number)

    return output


NT_RequestCirclePosition = lib.NT_RequestCirclePosition
NT_RequestCirclePosition.restype = c_short
NT_RequestCirclePosition.argtypes = [POINTER(c_char)]


def request_circle_position(serial_number):
    '''
    Requests the current scan circle centre position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestCirclePosition(serial_number)

    return output


NT_RequestControlMode = lib.NT_RequestControlMode
NT_RequestControlMode.restype = c_short
NT_RequestControlMode.argtypes = [POINTER(c_char)]


def request_control_mode(serial_number):
    '''
    Request the NanoTrak control mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestControlMode(serial_number)

    return output


NT_RequestFeedbackSource = lib.NT_RequestFeedbackSource
NT_RequestFeedbackSource.restype = c_short
NT_RequestFeedbackSource.argtypes = [POINTER(c_char)]


def request_feedback_source(serial_number):
    '''
    Requests the NanoTrak Feedback Source.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestFeedbackSource(serial_number)

    return output


NT_RequestGain = lib.NT_RequestGain
NT_RequestGain.restype = c_short
NT_RequestGain.argtypes = [POINTER(c_char)]


def request_gain(serial_number):
    '''
    Requests the control loop gain.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestGain(serial_number)

    return output


NT_RequestMaxTravel = lib.NT_RequestMaxTravel
NT_RequestMaxTravel.restype = c_short
NT_RequestMaxTravel.argtypes = [POINTER(c_char)]


def request_max_travel(serial_number):
    '''
    Requests the MaxTravel for the Piezos in um.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestMaxTravel(serial_number)

    return output


NT_RequestMode = lib.NT_RequestMode
NT_RequestMode.restype = c_short
NT_RequestMode.argtypes = [POINTER(c_char)]


def request_mode(serial_number):
    '''
    Requests the NanoTrak mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestMode(serial_number)

    return output


NT_RequestNTChannels = lib.NT_RequestNTChannels
NT_RequestNTChannels.restype = c_short
NT_RequestNTChannels.argtypes = [POINTER(c_char)]


def request_n_t_channels(serial_number):
    '''
    Request the device updates the NanoTrak channel numbers.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestNTChannels(serial_number)

    return output


NT_RequestPhaseCompensationParams = lib.NT_RequestPhaseCompensationParams
NT_RequestPhaseCompensationParams.restype = c_short
NT_RequestPhaseCompensationParams.argtypes = [POINTER(c_char)]


def request_phase_compensation_params(serial_number):
    '''
    Requests the phase compensation parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestPhaseCompensationParams(serial_number)

    return output


NT_RequestReading = lib.NT_RequestReading
NT_RequestReading.restype = c_short
NT_RequestReading.argtypes = [POINTER(c_char)]


def request_reading(serial_number):
    '''
    Requests a TIA reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestReading(serial_number)

    return output


NT_RequestSettings = lib.NT_RequestSettings
NT_RequestSettings.restype = c_short
NT_RequestSettings.argtypes = [POINTER(c_char)]


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

    output = NT_RequestSettings(serial_number)

    return output


NT_RequestSignalState = lib.NT_RequestSignalState
NT_RequestSignalState.restype = c_short
NT_RequestSignalState.argtypes = [POINTER(c_char)]


def request_signal_state(serial_number):
    '''
    Requests the NanoTrak signal state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestSignalState(serial_number)

    return output


NT_RequestStatus = lib.NT_RequestStatus
NT_RequestStatus.restype = c_short
NT_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    '''
    Requests the status bits and reading.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestStatus(serial_number)

    return output


NT_RequestStatusBits = lib.NT_RequestStatusBits
NT_RequestStatusBits.restype = c_short
NT_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    output = NT_RequestStatusBits(serial_number)

    return output


NT_RequestTIALPFilterParams = lib.NT_RequestTIALPFilterParams
NT_RequestTIALPFilterParams.restype = c_short
NT_RequestTIALPFilterParams.argtypes = [POINTER(c_char)]


def request_t_i_a_l_p_filter_params(serial_number):
    '''
    Requests the NanoTrak tracking threshold signal.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestTIALPFilterParams(serial_number)

    return output


NT_RequestTIArangeParams = lib.NT_RequestTIArangeParams
NT_RequestTIArangeParams.restype = c_short
NT_RequestTIArangeParams.argtypes = [POINTER(c_char)]


def request_t_i_arange_params(serial_number):
    '''
    Requests the TIA range parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestTIArangeParams(serial_number)

    return output


NT_RequestTrackingThresholdSignal = lib.NT_RequestTrackingThresholdSignal
NT_RequestTrackingThresholdSignal.restype = c_short
NT_RequestTrackingThresholdSignal.argtypes = [POINTER(c_char)]


def request_tracking_threshold_signal(serial_number):
    '''
    Requests the NanoTrak tracking threshold signal.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestTrackingThresholdSignal(serial_number)

    return output


NT_SetCircleDiameter = lib.NT_SetCircleDiameter
NT_SetCircleDiameter.restype = c_short
NT_SetCircleDiameter.argtypes = [POINTER(c_char)]


def set_circle_diameter(serial_number):
    '''
    Sets the scan circle diameter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        diameter: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    diameter = c_long()

    output = NT_SetCircleDiameter(serial_number)

    return output


NT_SetCircleDiameterLUT = lib.NT_SetCircleDiameterLUT
NT_SetCircleDiameterLUT.restype = c_short
NT_SetCircleDiameterLUT.argtypes = [POINTER(c_char)]


def set_circle_diameter_l_u_t(serial_number):
    '''
    Sets the scan circle diameter Lookup Table (LUT).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        LUT: NT_CircleDiameterLUT

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    LUT = NT_CircleDiameterLUT()

    output = NT_SetCircleDiameterLUT(serial_number)

    return output


NT_SetCircleHomePosition = lib.NT_SetCircleHomePosition
NT_SetCircleHomePosition.restype = c_short
NT_SetCircleHomePosition.argtypes = [POINTER(c_char)]


def set_circle_home_position(serial_number):
    '''
    Sets the home position of the scan circle.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: NT_HVComponent

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = NT_HVComponent()

    output = NT_SetCircleHomePosition(serial_number)

    return output


NT_SetCircleParams = lib.NT_SetCircleParams
NT_SetCircleParams.restype = c_short
NT_SetCircleParams.argtypes = [POINTER(c_char)]


def set_circle_params(serial_number):
    '''
    Sets the scanning circle parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_CircleParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_CircleParameters()

    output = NT_SetCircleParams(serial_number)

    return output


NT_SetControlMode = lib.NT_SetControlMode
NT_SetControlMode.restype = c_short
NT_SetControlMode.argtypes = [POINTER(c_char)]


def set_control_mode(serial_number):
    '''
    Set the NanoTrak control mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_long
        mode: NT_ControlMode

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_long()
    mode = NT_ControlMode()

    output = NT_SetControlMode(serial_number)

    return output


NT_SetFeedbackSource = lib.NT_SetFeedbackSource
NT_SetFeedbackSource.restype = c_short
NT_SetFeedbackSource.argtypes = [POINTER(c_char)]


def set_feedback_source(serial_number):
    '''
    Sets the NanoTrak feedback source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        input: NT_FeedbackSource
        input: KNA_FeedbackSource

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    input = NT_FeedbackSource()
    input = KNA_FeedbackSource()

    output = NT_SetFeedbackSource(serial_number)

    return output


NT_SetGain = lib.NT_SetGain
NT_SetGain.restype = c_short
NT_SetGain.argtypes = [POINTER(c_char)]


def set_gain(serial_number):
    '''
    Sets the control loop gain.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        gain: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    gain = c_short()

    output = NT_SetGain(serial_number)

    return output


NT_SetMode = lib.NT_SetMode
NT_SetMode.restype = c_short
NT_SetMode.argtypes = [POINTER(c_char)]


def set_mode(serial_number):
    '''
    Setsthe nanoTrak operating mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: NT_Mode

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = NT_Mode()

    output = NT_SetMode(serial_number)

    return output


NT_SetNTChannels = lib.NT_SetNTChannels
NT_SetNTChannels.restype = c_short
NT_SetNTChannels.argtypes = [POINTER(c_char)]


def set_n_t_channels(serial_number):
    '''
    Sets the NanoTrak channels to (usually) piezos.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        chanA: c_short
        chanB: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    chanA = c_short()
    chanB = c_short()

    output = NT_SetNTChannels(serial_number)

    return output


NT_SetPhaseCompensationParams = lib.NT_SetPhaseCompensationParams
NT_SetPhaseCompensationParams.restype = c_short
NT_SetPhaseCompensationParams.argtypes = [POINTER(c_char)]


def set_phase_compensation_params(serial_number):
    '''
    Sets the phase compensation parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_HVComponent

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_HVComponent()

    output = NT_SetPhaseCompensationParams(serial_number)

    return output


NT_SetRangeMode = lib.NT_SetRangeMode
NT_SetRangeMode.restype = c_short
NT_SetRangeMode.argtypes = [POINTER(c_char)]


def set_range_mode(serial_number):
    '''
    Get the TIA Range Mode and OddEven mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: NT_TIARangeMode
        oddOrEven: NT_OddOrEven

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mode = NT_TIARangeMode()
    oddOrEven = NT_OddOrEven()

    output = NT_SetRangeMode(serial_number)

    return output


NT_SetTIALPFilterParams = lib.NT_SetTIALPFilterParams
NT_SetTIALPFilterParams.restype = c_short
NT_SetTIALPFilterParams.argtypes = [POINTER(c_char)]


def set_t_i_a_l_p_filter_params(serial_number):
    '''
    Sets the TIA long pass filter parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_LowPassFilterParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_LowPassFilterParameters()

    output = NT_SetTIALPFilterParams(serial_number)

    return output


NT_SetTIARange = lib.NT_SetTIARange
NT_SetTIARange.restype = c_short
NT_SetTIARange.argtypes = [POINTER(c_char)]


def set_t_i_a_range(serial_number):
    '''
    Sets TIA range.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        range: NT_TIARange
        range: KNA_TIARange

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    range = NT_TIARange()
    range = KNA_TIARange()

    output = NT_SetTIARange(serial_number)

    return output


NT_SetTIArangeParams = lib.NT_SetTIArangeParams
NT_SetTIArangeParams.restype = c_short
NT_SetTIArangeParams.argtypes = [POINTER(c_char)]


def set_t_i_arange_params(serial_number):
    '''
    Sets the TIA range parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        params: NT_TIARangeParameters
        params: KNA_TIARangeParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    params = NT_TIARangeParameters()
    params = KNA_TIARangeParameters()

    output = NT_SetTIArangeParams(serial_number)

    return output


NT_SetTrackingThresholdSignal = lib.NT_SetTrackingThresholdSignal
NT_SetTrackingThresholdSignal.restype = c_short
NT_SetTrackingThresholdSignal.argtypes = [POINTER(c_char)]


def set_tracking_threshold_signal(serial_number):
    '''
    Sets the tracking threshold signal.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        threshold: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    threshold = c_float()

    output = NT_SetTrackingThresholdSignal(serial_number)

    return output


NT_StartPolling = lib.NT_StartPolling
NT_StartPolling.restype = c_bool
NT_StartPolling.argtypes = [POINTER(c_char)]


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

    output = NT_StartPolling(serial_number)

    return output


NT_StopPolling = lib.NT_StopPolling
NT_StopPolling.restype = c_void_p
NT_StopPolling.argtypes = [POINTER(c_char)]


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

    output = NT_StopPolling(serial_number)

    return output


NT_TimeSinceLastMsgReceived = lib.NT_TimeSinceLastMsgReceived
NT_TimeSinceLastMsgReceived.restype = c_bool
NT_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char)]


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

    output = NT_TimeSinceLastMsgReceived(serial_number)

    return output



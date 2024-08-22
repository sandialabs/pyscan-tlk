from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_float,
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
    KNA_Channels,
    KNA_FeedbackModeTypes,
    KNA_FeedbackSource,
    KNA_HighOutputVoltageRoute,
    KNA_HighVoltageRange,
    KNA_TIARange,
    KNA_TriggerPortMode,
    KNA_TriggerPortPolarity,
    KNA_WheelAdjustRate,
    NT_FeedbackSource,
    NT_Mode,
    NT_OddOrEven,
    NT_OutputVoltageRoute,
    NT_TIARange,
    NT_TIARangeMode,
    NT_VoltageRange)
from .definitions.structures import (
    BNT_IO_Settings,
    KNA_FeedbackLoopConstants,
    KNA_IOSettings,
    KNA_MMIParams,
    KNA_TIARangeParameters,
    KNA_TIAReading,
    KNA_TriggerConfig,
    NT_CircleDiameterLUT,
    NT_CircleParameters,
    NT_HVComponent,
    NT_IOSettings,
    NT_TIARangeParameters,
    NT_TIAReading,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.KCube.NanoTrak.DLL")

NT_CanDeviceLockFrontPanel = lib.NT_CanDeviceLockFrontPanel
NT_CanDeviceLockFrontPanel.restype = c_bool
NT_CanDeviceLockFrontPanel.argtypes = [POINTER(c_char)]


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

    output = NT_CanDeviceLockFrontPanel(serial_number)

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


NT_GetFeedbackLoopPIconsts = lib.NT_GetFeedbackLoopPIconsts
NT_GetFeedbackLoopPIconsts.restype = c_short
NT_GetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def get_feedback_loop_p_iconsts(serial_number):
    '''
    Gets the feedback loop constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels
        proportionalTerm: c_short
        integralTerm: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = NT_GetFeedbackLoopPIconsts(serial_number)

    return output


NT_GetFeedbackLoopPIconstsBlock = lib.NT_GetFeedbackLoopPIconstsBlock
NT_GetFeedbackLoopPIconstsBlock.restype = c_short
NT_GetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


def get_feedback_loop_p_iconsts_block(serial_number):
    '''
    Gets the feedback loop constants in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels
        proportionalAndIntegralConstants: KNA_FeedbackLoopConstants

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()
    proportionalAndIntegralConstants = KNA_FeedbackLoopConstants()

    output = NT_GetFeedbackLoopPIconstsBlock(serial_number)

    return output


NT_GetFeedbackMode = lib.NT_GetFeedbackMode
NT_GetFeedbackMode.restype = KNA_FeedbackModeTypes
NT_GetFeedbackMode.argtypes = [POINTER(c_char)]


def get_feedback_mode(serial_number):
    '''
    Gets the feedback mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels

    Returns
    -------
        KNA_FeedbackModeTypes
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()

    output = NT_GetFeedbackMode(serial_number)

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


NT_GetFrontPanelLocked = lib.NT_GetFrontPanelLocked
NT_GetFrontPanelLocked.restype = c_bool
NT_GetFrontPanelLocked.argtypes = [POINTER(c_char)]


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

    output = NT_GetFrontPanelLocked(serial_number)

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


NT_GetIOsettings = lib.NT_GetIOsettings
NT_GetIOsettings.restype = c_short
NT_GetIOsettings.argtypes = [POINTER(c_char)]


def get_i_osettings(serial_number):
    '''
    Gets the input/output options.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        highVoltageOutRange: KNA_HighVoltageRange
        lowVoltageOutRange: NT_VoltageRange
        highVoltageOutputRoute: KNA_HighOutputVoltageRoute
        lowVoltageOutputRoute: NT_OutputVoltageRoute

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    highVoltageOutRange = KNA_HighVoltageRange()
    lowVoltageOutRange = NT_VoltageRange()
    highVoltageOutputRoute = KNA_HighOutputVoltageRoute()
    lowVoltageOutputRoute = NT_OutputVoltageRoute()

    output = NT_GetIOsettings(serial_number)

    return output


NT_GetIOsettingsBlock = lib.NT_GetIOsettingsBlock
NT_GetIOsettingsBlock.restype = c_short
NT_GetIOsettingsBlock.argtypes = [POINTER(c_char)]


def get_i_osettings_block(serial_number):
    '''
    Gets the input/output settings in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        IOsettings: BNT_IO_Settings
        IOsettings: KNA_IOSettings
        IOsettings: NT_IOSettings
        channel: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    IOsettings = BNT_IO_Settings()
    IOsettings = KNA_IOSettings()
    IOsettings = NT_IOSettings()
    channel = c_long()

    output = NT_GetIOsettingsBlock(serial_number)

    return output


NT_GetLEDBrightness = lib.NT_GetLEDBrightness
NT_GetLEDBrightness.restype = c_short
NT_GetLEDBrightness.argtypes = [POINTER(c_char)]


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

    output = NT_GetLEDBrightness(serial_number)

    return output


NT_GetMMIParams = lib.NT_GetMMIParams
NT_GetMMIParams.restype = c_short
NT_GetMMIParams.argtypes = [POINTER(c_char)]


def get_m_m_i_params(serial_number):
    '''
    Get the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelAdjustRate: KNA_WheelAdjustRate
        displayIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    wheelAdjustRate = KNA_WheelAdjustRate()
    displayIntensity = c_int16()

    output = NT_GetMMIParams(serial_number)

    return output


NT_GetMMIParamsBlock = lib.NT_GetMMIParamsBlock
NT_GetMMIParamsBlock.restype = c_short
NT_GetMMIParamsBlock.argtypes = [POINTER(c_char)]


def get_m_m_i_params_block(serial_number):
    '''
    Gets the MMI parameters for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mmiParams: KNA_MMIParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mmiParams = KNA_MMIParams()

    output = NT_GetMMIParamsBlock(serial_number)

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


NT_GetTriggerConfigParams = lib.NT_GetTriggerConfigParams
NT_GetTriggerConfigParams.restype = c_short
NT_GetTriggerConfigParams.argtypes = [POINTER(c_char)]


def get_trigger_config_params(serial_number):
    '''
    Get the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KNA_TriggerPortMode
        trigger1Polarity: KNA_TriggerPortPolarity
        trigger2Mode: KNA_TriggerPortMode
        trigger2Polarity: KNA_TriggerPortPolarity

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    trigger1Mode = KNA_TriggerPortMode()
    trigger1Polarity = KNA_TriggerPortPolarity()
    trigger2Mode = KNA_TriggerPortMode()
    trigger2Polarity = KNA_TriggerPortPolarity()

    output = NT_GetTriggerConfigParams(serial_number)

    return output


NT_GetTriggerConfigParamsBlock = lib.NT_GetTriggerConfigParamsBlock
NT_GetTriggerConfigParamsBlock.restype = c_short
NT_GetTriggerConfigParamsBlock.argtypes = [POINTER(c_char)]


def get_trigger_config_params_block(serial_number):
    '''
    Gets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KNA_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerConfigParams = KNA_TriggerConfig()

    output = NT_GetTriggerConfigParamsBlock(serial_number)

    return output


NT_GetXYScanLine = lib.NT_GetXYScanLine
NT_GetXYScanLine.restype = c_short
NT_GetXYScanLine.argtypes = [POINTER(c_char)]


def get_x_y_scan_line(serial_number):
    '''
    Gets XY scan line.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        lineNo: c_int
        line: c_byte
        bufferSize: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    lineNo = c_int()
    line = c_byte()
    bufferSize = c_int()

    output = NT_GetXYScanLine(serial_number)

    return output


NT_GetXYScanRange = lib.NT_GetXYScanRange
NT_GetXYScanRange.restype = KNA_TIARange
NT_GetXYScanRange.argtypes = [POINTER(c_char)]


def get_x_y_scan_range(serial_number):
    '''
    Gets XY scan range.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        KNA_TIARange
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_GetXYScanRange(serial_number)

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


NT_IsXYScanAvailable = lib.NT_IsXYScanAvailable
NT_IsXYScanAvailable.restype = c_bool
NT_IsXYScanAvailable.argtypes = [POINTER(c_char)]


def is_x_y_scan_available(serial_number):
    '''
    Queries if the XY scan is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_IsXYScanAvailable(serial_number)

    return output


NT_IsXYScanLineAvailable = lib.NT_IsXYScanLineAvailable
NT_IsXYScanLineAvailable.restype = c_bool
NT_IsXYScanLineAvailable.argtypes = [POINTER(c_char)]


def is_x_y_scan_line_available(serial_number):
    '''
    Queries if an XY scan line is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        lineNo: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    lineNo = c_int()

    output = NT_IsXYScanLineAvailable(serial_number)

    return output


NT_IsXYScanning = lib.NT_IsXYScanning
NT_IsXYScanning.restype = c_bool
NT_IsXYScanning.argtypes = [POINTER(c_char)]


def is_x_y_scanning(serial_number):
    '''
    Query if the device is XY scanning.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_IsXYScanning(serial_number)

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


NT_PersistSettings = lib.NT_PersistSettings
NT_PersistSettings.restype = c_bool
NT_PersistSettings.argtypes = [POINTER(c_char)]


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

    output = NT_PersistSettings(serial_number)

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


NT_RequestFeedbackLoopPIconsts = lib.NT_RequestFeedbackLoopPIconsts
NT_RequestFeedbackLoopPIconsts.restype = c_bool
NT_RequestFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def request_feedback_loop_p_iconsts(serial_number):
    '''
    Requests that the feedback loop constants be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()

    output = NT_RequestFeedbackLoopPIconsts(serial_number)

    return output


NT_RequestFeedbackMode = lib.NT_RequestFeedbackMode
NT_RequestFeedbackMode.restype = c_bool
NT_RequestFeedbackMode.argtypes = [POINTER(c_char)]


def request_feedback_mode(serial_number):
    '''
    Requests the feedback mode from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()

    output = NT_RequestFeedbackMode(serial_number)

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


NT_RequestFrontPanelLocked = lib.NT_RequestFrontPanelLocked
NT_RequestFrontPanelLocked.restype = c_short
NT_RequestFrontPanelLocked.argtypes = [POINTER(c_char)]


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

    output = NT_RequestFrontPanelLocked(serial_number)

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


NT_RequestIOsettings = lib.NT_RequestIOsettings
NT_RequestIOsettings.restype = c_short
NT_RequestIOsettings.argtypes = [POINTER(c_char)]


def request_i_osettings(serial_number):
    '''
    Requests the input/output options.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestIOsettings(serial_number)

    return output


NT_RequestMMIParams = lib.NT_RequestMMIParams
NT_RequestMMIParams.restype = c_bool
NT_RequestMMIParams.argtypes = [POINTER(c_char)]


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

    output = NT_RequestMMIParams(serial_number)

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


NT_RequestTriggerConfigParams = lib.NT_RequestTriggerConfigParams
NT_RequestTriggerConfigParams.restype = c_bool
NT_RequestTriggerConfigParams.argtypes = [POINTER(c_char)]


def request_trigger_config_params(serial_number):
    '''
    Requests that the trigger config parameters are read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestTriggerConfigParams(serial_number)

    return output


NT_RequestXYScan = lib.NT_RequestXYScan
NT_RequestXYScan.restype = c_short
NT_RequestXYScan.argtypes = [POINTER(c_char)]


def request_x_y_scan(serial_number):
    '''
    Request an XY scan.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_RequestXYScan(serial_number)

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


NT_SetFeedbackLoopPIconsts = lib.NT_SetFeedbackLoopPIconsts
NT_SetFeedbackLoopPIconsts.restype = c_short
NT_SetFeedbackLoopPIconsts.argtypes = [POINTER(c_char)]


def set_feedback_loop_p_iconsts(serial_number):
    '''
    Sets the feedback loop constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels
        proportionalTerm: c_short
        integralTerm: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()
    proportionalTerm = c_short()
    integralTerm = c_short()

    output = NT_SetFeedbackLoopPIconsts(serial_number)

    return output


NT_SetFeedbackLoopPIconstsBlock = lib.NT_SetFeedbackLoopPIconstsBlock
NT_SetFeedbackLoopPIconstsBlock.restype = c_short
NT_SetFeedbackLoopPIconstsBlock.argtypes = [POINTER(c_char)]


def set_feedback_loop_p_iconsts_block(serial_number):
    '''
    Sets the feedback loop constants in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels
        proportionalAndIntegralConstants: KNA_FeedbackLoopConstants

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()
    proportionalAndIntegralConstants = KNA_FeedbackLoopConstants()

    output = NT_SetFeedbackLoopPIconstsBlock(serial_number)

    return output


NT_SetFeedbackMode = lib.NT_SetFeedbackMode
NT_SetFeedbackMode.restype = c_short
NT_SetFeedbackMode.argtypes = [POINTER(c_char)]


def set_feedback_mode(serial_number):
    '''
    Sets the feedback mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: KNA_Channels
        mode: KNA_FeedbackModeTypes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = KNA_Channels()
    mode = KNA_FeedbackModeTypes()

    output = NT_SetFeedbackMode(serial_number)

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


NT_SetFrontPanelLock = lib.NT_SetFrontPanelLock
NT_SetFrontPanelLock.restype = c_short
NT_SetFrontPanelLock.argtypes = [POINTER(c_char)]


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

    output = NT_SetFrontPanelLock(serial_number)

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


NT_SetIOsettings = lib.NT_SetIOsettings
NT_SetIOsettings.restype = c_short
NT_SetIOsettings.argtypes = [POINTER(c_char)]


def set_i_osettings(serial_number):
    '''
    Sets the input/output options.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        highVoltageOutRange: KNA_HighVoltageRange
        lowVoltageOutRange: NT_VoltageRange
        highVoltageOutputRoute: KNA_HighOutputVoltageRoute
        lowVoltageOutputRoute: NT_OutputVoltageRoute

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    highVoltageOutRange = KNA_HighVoltageRange()
    lowVoltageOutRange = NT_VoltageRange()
    highVoltageOutputRoute = KNA_HighOutputVoltageRoute()
    lowVoltageOutputRoute = NT_OutputVoltageRoute()

    output = NT_SetIOsettings(serial_number)

    return output


NT_SetIOsettingsBlock = lib.NT_SetIOsettingsBlock
NT_SetIOsettingsBlock.restype = c_short
NT_SetIOsettingsBlock.argtypes = [POINTER(c_char)]


def set_i_osettings_block(serial_number):
    '''
    Sets the input/output options in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        IOsettings: BNT_IO_Settings
        IOsettings: KNA_IOSettings
        IOsettings: NT_IOSettings
        channel: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    IOsettings = BNT_IO_Settings()
    IOsettings = KNA_IOSettings()
    IOsettings = NT_IOSettings()
    channel = c_long()

    output = NT_SetIOsettingsBlock(serial_number)

    return output


NT_SetLEDBrightness = lib.NT_SetLEDBrightness
NT_SetLEDBrightness.restype = c_short
NT_SetLEDBrightness.argtypes = [POINTER(c_char)]


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

    output = NT_SetLEDBrightness(serial_number)

    return output


NT_SetMMIParams = lib.NT_SetMMIParams
NT_SetMMIParams.restype = c_short
NT_SetMMIParams.argtypes = [POINTER(c_char)]


def set_m_m_i_params(serial_number):
    '''
    Set the MMI Parameters for the KCube Display Interface.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        wheelAdjustRate: KNA_WheelAdjustRate
        displayIntensity: c_int16

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    wheelAdjustRate = KNA_WheelAdjustRate()
    displayIntensity = c_int16()

    output = NT_SetMMIParams(serial_number)

    return output


NT_SetMMIParamsBlock = lib.NT_SetMMIParamsBlock
NT_SetMMIParamsBlock.restype = c_short
NT_SetMMIParamsBlock.argtypes = [POINTER(c_char)]


def set_m_m_i_params_block(serial_number):
    '''
    Sets the MMI parameters for the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mmiParams: KNA_MMIParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    mmiParams = KNA_MMIParams()

    output = NT_SetMMIParamsBlock(serial_number)

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


NT_SetTriggerConfigParams = lib.NT_SetTriggerConfigParams
NT_SetTriggerConfigParams.restype = c_short
NT_SetTriggerConfigParams.argtypes = [POINTER(c_char)]


def set_trigger_config_params(serial_number):
    '''
    Set the Trigger Configuration Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        trigger1Mode: KNA_TriggerPortMode
        trigger1Polarity: KNA_TriggerPortPolarity
        trigger2Mode: KNA_TriggerPortMode
        trigger2Polarity: KNA_TriggerPortPolarity

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    trigger1Mode = KNA_TriggerPortMode()
    trigger1Polarity = KNA_TriggerPortPolarity()
    trigger2Mode = KNA_TriggerPortMode()
    trigger2Polarity = KNA_TriggerPortPolarity()

    output = NT_SetTriggerConfigParams(serial_number)

    return output


NT_SetTriggerConfigParamsBlock = lib.NT_SetTriggerConfigParamsBlock
NT_SetTriggerConfigParamsBlock.restype = c_short
NT_SetTriggerConfigParamsBlock.argtypes = [POINTER(c_char)]


def set_trigger_config_params_block(serial_number):
    '''
    Sets the trigger configuration parameters block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        triggerConfigParams: KNA_TriggerConfig

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    triggerConfigParams = KNA_TriggerConfig()

    output = NT_SetTriggerConfigParamsBlock(serial_number)

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


NT_StopXYScan = lib.NT_StopXYScan
NT_StopXYScan.restype = c_short
NT_StopXYScan.argtypes = [POINTER(c_char)]


def stop_x_y_scan(serial_number):
    '''
    Stops an XY scan.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = NT_StopXYScan(serial_number)

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


NT_WaitForMessage = lib.NT_WaitForMessage
NT_WaitForMessage.restype = c_bool
NT_WaitForMessage.argtypes = [POINTER(c_char)]


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

    output = NT_WaitForMessage(serial_number)

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



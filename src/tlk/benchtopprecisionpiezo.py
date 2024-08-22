from ctypes import (
    POINTER,
    c_byte,
    c_char,
    c_char_p,
    c_int,
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
    PPC_IOSettings,
    PPC_NotchParams,
    PPC_PIDConsts,
    TLI_DeviceInfo,
    TLI_HardwareInformation)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Benchtop.PrecisionPiezo.dll")

PPC2_ClearMessageQueue = lib.PPC2_ClearMessageQueue
PPC2_ClearMessageQueue.restype = c_short
PPC2_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue2(serial_number):
    '''
    Clears the device message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_ClearMessageQueue(serial_number)

    return output


PPC2_DisableChannel = lib.PPC2_DisableChannel
PPC2_DisableChannel.restype = c_short
PPC2_DisableChannel.argtypes = [POINTER(c_char)]


def disable_channel2(serial_number):
    '''
    Disable the channel so that motor can be moved by hand.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_DisableChannel(serial_number)

    return output


PPC2_EnableChannel = lib.PPC2_EnableChannel
PPC2_EnableChannel.restype = c_short
PPC2_EnableChannel.argtypes = [POINTER(c_char)]


def enable_channel2(serial_number):
    '''
    Enable channel for computer control.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_EnableChannel(serial_number)

    return output


PPC2_GetHardwareInfo = lib.PPC2_GetHardwareInfo
PPC2_GetHardwareInfo.restype = c_short
PPC2_GetHardwareInfo.argtypes = [POINTER(c_char)]


def get_hardware_info2(serial_number):
    '''
    Gets the hardware information from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
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
    channel = c_int()
    modelNo = POINTER(c_char)()
    sizeOfModelNo = c_ulong()
    type = c_long()
    numChannels = c_long()
    notes = POINTER(c_char)()
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = PPC2_GetHardwareInfo(serial_number)

    return output


PPC2_GetHardwareInfoBlock = lib.PPC2_GetHardwareInfoBlock
PPC2_GetHardwareInfoBlock.restype = c_short
PPC2_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


def get_hardware_info_block2(serial_number):
    '''
    Gets the hardware information in a block.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        hardwareInfo: TLI_HardwareInformation

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    hardwareInfo = TLI_HardwareInformation()

    output = PPC2_GetHardwareInfoBlock(serial_number)

    return output


PPC2_GetIOSettings = lib.PPC2_GetIOSettings
PPC2_GetIOSettings.restype = c_short
PPC2_GetIOSettings.argtypes = [POINTER(c_char)]


def get_i_o_settings2(serial_number):
    '''
    Gets the PPC IO Settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        ioSettings: PPC_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    ioSettings = PPC_IOSettings()

    output = PPC2_GetIOSettings(serial_number)

    return output


PPC2_GetMaxOutputVoltage = lib.PPC2_GetMaxOutputVoltage
PPC2_GetMaxOutputVoltage.restype = c_short
PPC2_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def get_max_output_voltage2(serial_number):
    '''
    Gets the maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetMaxOutputVoltage(serial_number)

    return output


PPC2_GetMaximumTravel = lib.PPC2_GetMaximumTravel
PPC2_GetMaximumTravel.restype = c_long
PPC2_GetMaximumTravel.argtypes = [POINTER(c_char)]


def get_maximum_travel2(serial_number):
    '''
    Gets the maximum travel of the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetMaximumTravel(serial_number)

    return output


PPC2_GetMinOutputVoltage = lib.PPC2_GetMinOutputVoltage
PPC2_GetMinOutputVoltage.restype = c_short
PPC2_GetMinOutputVoltage.argtypes = [POINTER(c_char)]


def get_min_output_voltage2(serial_number):
    '''
    Gets the minimum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetMinOutputVoltage(serial_number)

    return output


PPC2_GetNextMessage = lib.PPC2_GetNextMessage
PPC2_GetNextMessage.restype = c_bool
PPC2_GetNextMessage.argtypes = [POINTER(c_char)]


def get_next_message2(serial_number):
    '''
    Get the next MessageQueue item if it is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PPC2_GetNextMessage(serial_number)

    return output


PPC2_GetNotchParams = lib.PPC2_GetNotchParams
PPC2_GetNotchParams.restype = c_short
PPC2_GetNotchParams.argtypes = [POINTER(c_char)]


def get_notch_params2(serial_number):
    '''
    Gets the PPC Notch Filter Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        notchParams: PPC_NotchParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    notchParams = PPC_NotchParams()

    output = PPC2_GetNotchParams(serial_number)

    return output


PPC2_GetOutputVoltage = lib.PPC2_GetOutputVoltage
PPC2_GetOutputVoltage.restype = c_short
PPC2_GetOutputVoltage.argtypes = [POINTER(c_char)]


def get_output_voltage2(serial_number):
    '''
    Gets the set Output Voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetOutputVoltage(serial_number)

    return output


PPC2_GetPIDConsts = lib.PPC2_GetPIDConsts
PPC2_GetPIDConsts.restype = c_short
PPC2_GetPIDConsts.argtypes = [POINTER(c_char)]


def get_p_i_d_consts2(serial_number):
    '''
    Gets the PPC PID Constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        pidConsts: PPC_PIDConsts

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    pidConsts = PPC_PIDConsts()

    output = PPC2_GetPIDConsts(serial_number)

    return output


PPC2_GetPosition = lib.PPC2_GetPosition
PPC2_GetPosition.restype = c_short
PPC2_GetPosition.argtypes = [POINTER(c_char)]


def get_position2(serial_number):
    '''
    Gets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetPosition(serial_number)

    return output


PPC2_GetPositionControlMode = lib.PPC2_GetPositionControlMode
PPC2_GetPositionControlMode.restype = PZ_ControlModeTypes
PPC2_GetPositionControlMode.argtypes = [POINTER(c_char)]


def get_position_control_mode2(serial_number):
    '''
    Gets the Position Control Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        PZ_ControlModeTypes
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetPositionControlMode(serial_number)

    return output


PPC2_GetRackDigitalOutputs = lib.PPC2_GetRackDigitalOutputs
PPC2_GetRackDigitalOutputs.restype = c_byte
PPC2_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def get_rack_digital_outputs2(serial_number):
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

    output = PPC2_GetRackDigitalOutputs(serial_number)

    return output


PPC2_GetRackStatusBits = lib.PPC2_GetRackStatusBits
PPC2_GetRackStatusBits.restype = c_ulong
PPC2_GetRackStatusBits.argtypes = [POINTER(c_char)]


def get_rack_status_bits2(serial_number):
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

    output = PPC2_GetRackStatusBits(serial_number)

    return output


PPC2_GetStatusBits = lib.PPC2_GetStatusBits
PPC2_GetStatusBits.restype = c_ulong
PPC2_GetStatusBits.argtypes = [POINTER(c_char)]


def get_status_bits2(serial_number):
    '''
    Get the current status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_ulong
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetStatusBits(serial_number)

    return output


PPC2_GetVoltageSource = lib.PPC2_GetVoltageSource
PPC2_GetVoltageSource.restype = PZ_InputSourceFlags
PPC2_GetVoltageSource.argtypes = [POINTER(c_char)]


def get_voltage_source2(serial_number):
    '''
    Gets the control voltage source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        PZ_InputSourceFlags
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_GetVoltageSource(serial_number)

    return output


PPC2_Identify = lib.PPC2_Identify
PPC2_Identify.restype = c_void_p
PPC2_Identify.argtypes = [POINTER(c_char)]


def identify2(serial_number):
    '''
    Sends a command to the device to make it identify iteself.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_Identify(serial_number)

    return output


PPC2_LoadNamedSettings = lib.PPC2_LoadNamedSettings
PPC2_LoadNamedSettings.restype = c_bool
PPC2_LoadNamedSettings.argtypes = [POINTER(c_char)]


def load_named_settings2(serial_number):
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

    output = PPC2_LoadNamedSettings(serial_number)

    return output


PPC2_LoadSettings = lib.PPC2_LoadSettings
PPC2_LoadSettings.restype = c_bool
PPC2_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings2(serial_number):
    '''
    Update device with stored settings.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_LoadSettings(serial_number)

    return output


PPC2_MessageQueueSize = lib.PPC2_MessageQueueSize
PPC2_MessageQueueSize.restype = c_int
PPC2_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size2(serial_number):
    '''
    Gets the MessageQueue size.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_int
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_MessageQueueSize(serial_number)

    return output


PPC2_PersistSettings = lib.PPC2_PersistSettings
PPC2_PersistSettings.restype = c_bool
PPC2_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings2(serial_number):
    '''
    Persist device settings to device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_PersistSettings(serial_number)

    return output


PPC2_PollingDuration = lib.PPC2_PollingDuration
PPC2_PollingDuration.restype = c_long
PPC2_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration2(serial_number):
    '''
    Gets the polling loop duration.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_PollingDuration(serial_number)

    return output


PPC2_RegisterMessageCallback = lib.PPC2_RegisterMessageCallback
PPC2_RegisterMessageCallback.restype = c_short
PPC2_RegisterMessageCallback.argtypes = [POINTER(c_char)]


def register_message_callback2(serial_number):
    '''
    Registers a callback on the message queue.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        None

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RegisterMessageCallback(serial_number)

    return output


PPC2_RequestActualPosition = lib.PPC2_RequestActualPosition
PPC2_RequestActualPosition.restype = c_short
PPC2_RequestActualPosition.argtypes = [POINTER(c_char)]


def request_actual_position2(serial_number):
    '''
    Requests the position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestActualPosition(serial_number)

    return output


PPC2_RequestMaxOutputVoltage = lib.PPC2_RequestMaxOutputVoltage
PPC2_RequestMaxOutputVoltage.restype = c_bool
PPC2_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]


def request_max_output_voltage2(serial_number):
    '''
    Requests the maximum output voltage be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestMaxOutputVoltage(serial_number)

    return output


PPC2_RequestOutputVoltage = lib.PPC2_RequestOutputVoltage
PPC2_RequestOutputVoltage.restype = c_bool
PPC2_RequestOutputVoltage.argtypes = [POINTER(c_char)]


def request_output_voltage2(serial_number):
    '''
    Requests the Output Voltage be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestOutputVoltage(serial_number)

    return output


PPC2_RequestPIDConsts = lib.PPC2_RequestPIDConsts
PPC2_RequestPIDConsts.restype = c_bool
PPC2_RequestPIDConsts.argtypes = [POINTER(c_char)]


def request_p_i_d_consts2(serial_number):
    '''
    Requests that the PPC PID Constants be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestPIDConsts(serial_number)

    return output


PPC2_RequestPosition = lib.PPC2_RequestPosition
PPC2_RequestPosition.restype = c_short
PPC2_RequestPosition.argtypes = [POINTER(c_char)]


def request_position2(serial_number):
    '''
    Requests the current output voltage or position depending on current mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestPosition(serial_number)

    return output


PPC2_RequestRackDigitalOutputs = lib.PPC2_RequestRackDigitalOutputs
PPC2_RequestRackDigitalOutputs.restype = c_short
PPC2_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]


def request_rack_digital_outputs2(serial_number):
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

    output = PPC2_RequestRackDigitalOutputs(serial_number)

    return output


PPC2_RequestRackStatusBits = lib.PPC2_RequestRackStatusBits
PPC2_RequestRackStatusBits.restype = c_short
PPC2_RequestRackStatusBits.argtypes = [POINTER(c_char)]


def request_rack_status_bits2(serial_number):
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

    output = PPC2_RequestRackStatusBits(serial_number)

    return output


PPC2_RequestSettings = lib.PPC2_RequestSettings
PPC2_RequestSettings.restype = c_short
PPC2_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings2(serial_number):
    '''
    Requests that all settings are download from device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestSettings(serial_number)

    return output


PPC2_RequestStatus = lib.PPC2_RequestStatus
PPC2_RequestStatus.restype = c_short
PPC2_RequestStatus.argtypes = [POINTER(c_char)]


def request_status2(serial_number):
    '''
    Requests the status bits and position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestStatus(serial_number)

    return output


PPC2_RequestStatusBits = lib.PPC2_RequestStatusBits
PPC2_RequestStatusBits.restype = c_short
PPC2_RequestStatusBits.argtypes = [POINTER(c_char)]


def request_status_bits2(serial_number):
    '''
    Request the status bits which identify the current device state.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestStatusBits(serial_number)

    return output


PPC2_RequestVoltageSource = lib.PPC2_RequestVoltageSource
PPC2_RequestVoltageSource.restype = c_bool
PPC2_RequestVoltageSource.argtypes = [POINTER(c_char)]


def request_voltage_source2(serial_number):
    '''
    Requests that the current input voltage source be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_RequestVoltageSource(serial_number)

    return output


PPC2_ResetParameters = lib.PPC2_ResetParameters
PPC2_ResetParameters.restype = c_short
PPC2_ResetParameters.argtypes = [POINTER(c_char)]


def reset_parameters2(serial_number):
    '''
    Resets all parameters to power-up values.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_ResetParameters(serial_number)

    return output


PPC2_SetIOSettings = lib.PPC2_SetIOSettings
PPC2_SetIOSettings.restype = c_short
PPC2_SetIOSettings.argtypes = [POINTER(c_char)]


def set_i_o_settings2(serial_number):
    '''
    Sets the PPC IO Setting.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        ioSettings: PPC_IOSettings

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    ioSettings = PPC_IOSettings()

    output = PPC2_SetIOSettings(serial_number)

    return output


PPC2_SetMaxOutputVoltage = lib.PPC2_SetMaxOutputVoltage
PPC2_SetMaxOutputVoltage.restype = c_short
PPC2_SetMaxOutputVoltage.argtypes = [POINTER(c_char)]


def set_max_output_voltage2(serial_number):
    '''
    Sets the maximum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        maxVoltage: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    maxVoltage = c_short()

    output = PPC2_SetMaxOutputVoltage(serial_number)

    return output


PPC2_SetNotchParams = lib.PPC2_SetNotchParams
PPC2_SetNotchParams.restype = c_short
PPC2_SetNotchParams.argtypes = [POINTER(c_char)]


def set_notch_params2(serial_number):
    '''
    Sets the PPC Notch Filter Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        notchParams: PPC_NotchParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    notchParams = PPC_NotchParams()

    output = PPC2_SetNotchParams(serial_number)

    return output


PPC2_SetOutputVoltage = lib.PPC2_SetOutputVoltage
PPC2_SetOutputVoltage.restype = c_short
PPC2_SetOutputVoltage.argtypes = [POINTER(c_char)]


def set_output_voltage2(serial_number):
    '''
    Sets the output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        volts: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    volts = c_short()

    output = PPC2_SetOutputVoltage(serial_number)

    return output


PPC2_SetPIDConsts = lib.PPC2_SetPIDConsts
PPC2_SetPIDConsts.restype = c_short
PPC2_SetPIDConsts.argtypes = [POINTER(c_char)]


def set_p_i_d_consts2(serial_number):
    '''
    Sets the PPC PID Constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        pidConsts: PPC_PIDConsts

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    pidConsts = PPC_PIDConsts()

    output = PPC2_SetPIDConsts(serial_number)

    return output


PPC2_SetPosition = lib.PPC2_SetPosition
PPC2_SetPosition.restype = c_short
PPC2_SetPosition.argtypes = [POINTER(c_char)]


def set_position2(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        position: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    position = c_short()

    output = PPC2_SetPosition(serial_number)

    return output


PPC2_SetPositionControlMode = lib.PPC2_SetPositionControlMode
PPC2_SetPositionControlMode.restype = c_short
PPC2_SetPositionControlMode.argtypes = [POINTER(c_char)]


def set_position_control_mode2(serial_number):
    '''
    Sets the Position Control Mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        mode: PZ_ControlModeTypes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    mode = PZ_ControlModeTypes()

    output = PPC2_SetPositionControlMode(serial_number)

    return output


PPC2_SetPositionToTolerance = lib.PPC2_SetPositionToTolerance
PPC2_SetPositionToTolerance.restype = c_short
PPC2_SetPositionToTolerance.argtypes = [POINTER(c_char)]


def set_position_to_tolerance2(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        position: c_short
        tolerance: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    position = c_short()
    tolerance = c_short()

    output = PPC2_SetPositionToTolerance(serial_number)

    return output


PPC2_SetRackDigitalOutputs = lib.PPC2_SetRackDigitalOutputs
PPC2_SetRackDigitalOutputs.restype = c_short
PPC2_SetRackDigitalOutputs.argtypes = [POINTER(c_char)]


def set_rack_digital_outputs2(serial_number):
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

    output = PPC2_SetRackDigitalOutputs(serial_number)

    return output


PPC2_SetVoltageSource = lib.PPC2_SetVoltageSource
PPC2_SetVoltageSource.restype = c_short
PPC2_SetVoltageSource.argtypes = [POINTER(c_char)]


def set_voltage_source2(serial_number):
    '''
    Sets the control voltage source.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        source: PZ_InputSourceFlags

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    source = PZ_InputSourceFlags()

    output = PPC2_SetVoltageSource(serial_number)

    return output


PPC2_SetZero = lib.PPC2_SetZero
PPC2_SetZero.restype = c_short
PPC2_SetZero.argtypes = [POINTER(c_char)]


def set_zero2(serial_number):
    '''
    Sets the voltage output to zero and defines the ensuing actuator position az zero.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_SetZero(serial_number)

    return output


PPC2_StartPolling = lib.PPC2_StartPolling
PPC2_StartPolling.restype = c_bool
PPC2_StartPolling.argtypes = [POINTER(c_char)]


def start_polling2(serial_number):
    '''
    Starts the internal polling loop which continuously requests position and status.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        milliseconds: c_int

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    milliseconds = c_int()

    output = PPC2_StartPolling(serial_number)

    return output


PPC2_StopPolling = lib.PPC2_StopPolling
PPC2_StopPolling.restype = c_void_p
PPC2_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling2(serial_number):
    '''
    Stops the internal polling loop.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()

    output = PPC2_StopPolling(serial_number)

    return output


PPC2_WaitForMessage = lib.PPC2_WaitForMessage
PPC2_WaitForMessage.restype = c_bool
PPC2_WaitForMessage.argtypes = [POINTER(c_char)]


def wait_for_message2(serial_number):
    '''
    Get the next MessageQueue item if it is available.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        channel: c_int
        messageType: c_long
        messageID: c_long
        messageData: c_ulong

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    channel = c_int()
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PPC2_WaitForMessage(serial_number)

    return output


PPC_CheckConnection = lib.PPC_CheckConnection
PPC_CheckConnection.restype = c_bool
PPC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = PPC_CheckConnection(serial_number)

    return output


PPC_ClearMessageQueue = lib.PPC_ClearMessageQueue
PPC_ClearMessageQueue.restype = c_short
PPC_ClearMessageQueue.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_ClearMessageQueue(serial_number)

    return output


PPC_Close = lib.PPC_Close
PPC_Close.restype = c_void_p
PPC_Close.argtypes = [POINTER(c_char)]


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

    output = PPC_Close(serial_number)

    return output


PPC_DisableChannel = lib.PPC_DisableChannel
PPC_DisableChannel.restype = c_short
PPC_DisableChannel.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_DisableChannel(serial_number)

    return output


PPC_Disconnect = lib.PPC_Disconnect
PPC_Disconnect.restype = c_short
PPC_Disconnect.argtypes = [POINTER(c_char)]


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

    output = PPC_Disconnect(serial_number)

    return output


PPC_EnableChannel = lib.PPC_EnableChannel
PPC_EnableChannel.restype = c_short
PPC_EnableChannel.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_EnableChannel(serial_number)

    return output


PPC_GetFirmwareVersion = lib.PPC_GetFirmwareVersion
PPC_GetFirmwareVersion.restype = c_ulong
PPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


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

    output = PPC_GetFirmwareVersion(serial_number)

    return output


PPC_GetHardwareInfo = lib.PPC_GetHardwareInfo
PPC_GetHardwareInfo.restype = c_short
PPC_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = PPC_GetHardwareInfo(serial_number)

    return output


PPC_GetHardwareInfoBlock = lib.PPC_GetHardwareInfoBlock
PPC_GetHardwareInfoBlock.restype = c_short
PPC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = PPC_GetHardwareInfoBlock(serial_number)

    return output


PPC_GetIOSettings = lib.PPC_GetIOSettings
PPC_GetIOSettings.restype = c_short
PPC_GetIOSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    ioSettings = PPC_IOSettings()

    output = PPC_GetIOSettings(serial_number)

    return output


PPC_GetMaxOutputVoltage = lib.PPC_GetMaxOutputVoltage
PPC_GetMaxOutputVoltage.restype = c_short
PPC_GetMaxOutputVoltage.argtypes = [POINTER(c_char)]


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

    output = PPC_GetMaxOutputVoltage(serial_number)

    return output


PPC_GetMaximumTravel = lib.PPC_GetMaximumTravel
PPC_GetMaximumTravel.restype = c_long
PPC_GetMaximumTravel.argtypes = [POINTER(c_char)]


def get_maximum_travel(serial_number):
    '''
    Gets the maximum travel of the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_GetMaximumTravel(serial_number)

    return output


PPC_GetMinOutputVoltage = lib.PPC_GetMinOutputVoltage
PPC_GetMinOutputVoltage.restype = c_short
PPC_GetMinOutputVoltage.argtypes = [POINTER(c_char)]


def get_min_output_voltage(serial_number):
    '''
    Gets the minimum output voltage.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_GetMinOutputVoltage(serial_number)

    return output


PPC_GetNextMessage = lib.PPC_GetNextMessage
PPC_GetNextMessage.restype = c_bool
PPC_GetNextMessage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PPC_GetNextMessage(serial_number)

    return output


PPC_GetNotchParams = lib.PPC_GetNotchParams
PPC_GetNotchParams.restype = c_short
PPC_GetNotchParams.argtypes = [POINTER(c_char)]


def get_notch_params(serial_number):
    '''
    Gets the PPC Notch Filter Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        notchParams: PPC_NotchParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    notchParams = PPC_NotchParams()

    output = PPC_GetNotchParams(serial_number)

    return output


PPC_GetOutputVoltage = lib.PPC_GetOutputVoltage
PPC_GetOutputVoltage.restype = c_short
PPC_GetOutputVoltage.argtypes = [POINTER(c_char)]


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

    output = PPC_GetOutputVoltage(serial_number)

    return output


PPC_GetPIDConsts = lib.PPC_GetPIDConsts
PPC_GetPIDConsts.restype = c_short
PPC_GetPIDConsts.argtypes = [POINTER(c_char)]


def get_p_i_d_consts(serial_number):
    '''
    Gets the PPC PID Constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        pidConsts: PPC_PIDConsts

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    pidConsts = PPC_PIDConsts()

    output = PPC_GetPIDConsts(serial_number)

    return output


PPC_GetPosition = lib.PPC_GetPosition
PPC_GetPosition.restype = c_short
PPC_GetPosition.argtypes = [POINTER(c_char)]


def get_position(serial_number):
    '''
    Gets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_GetPosition(serial_number)

    return output


PPC_GetPositionControlMode = lib.PPC_GetPositionControlMode
PPC_GetPositionControlMode.restype = PZ_ControlModeTypes
PPC_GetPositionControlMode.argtypes = [POINTER(c_char)]


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

    output = PPC_GetPositionControlMode(serial_number)

    return output


PPC_GetRackDigitalOutputs = lib.PPC_GetRackDigitalOutputs
PPC_GetRackDigitalOutputs.restype = c_byte
PPC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]


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

    output = PPC_GetRackDigitalOutputs(serial_number)

    return output


PPC_GetRackStatusBits = lib.PPC_GetRackStatusBits
PPC_GetRackStatusBits.restype = c_ulong
PPC_GetRackStatusBits.argtypes = [POINTER(c_char)]


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

    output = PPC_GetRackStatusBits(serial_number)

    return output


PPC_GetSoftwareVersion = lib.PPC_GetSoftwareVersion
PPC_GetSoftwareVersion.restype = c_ulong
PPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


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

    output = PPC_GetSoftwareVersion(serial_number)

    return output


PPC_GetStatusBits = lib.PPC_GetStatusBits
PPC_GetStatusBits.restype = c_ulong
PPC_GetStatusBits.argtypes = [POINTER(c_char)]


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

    output = PPC_GetStatusBits(serial_number)

    return output


PPC_GetVoltageSource = lib.PPC_GetVoltageSource
PPC_GetVoltageSource.restype = PZ_InputSourceFlags
PPC_GetVoltageSource.argtypes = [POINTER(c_char)]


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

    output = PPC_GetVoltageSource(serial_number)

    return output


PPC_Identify = lib.PPC_Identify
PPC_Identify.restype = c_void_p
PPC_Identify.argtypes = [POINTER(c_char)]


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

    output = PPC_Identify(serial_number)

    return output


PPC_LoadNamedSettings = lib.PPC_LoadNamedSettings
PPC_LoadNamedSettings.restype = c_bool
PPC_LoadNamedSettings.argtypes = [POINTER(c_char)]


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

    output = PPC_LoadNamedSettings(serial_number)

    return output


PPC_LoadSettings = lib.PPC_LoadSettings
PPC_LoadSettings.restype = c_bool
PPC_LoadSettings.argtypes = [POINTER(c_char)]


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

    output = PPC_LoadSettings(serial_number)

    return output


PPC_MessageQueueSize = lib.PPC_MessageQueueSize
PPC_MessageQueueSize.restype = c_int
PPC_MessageQueueSize.argtypes = [POINTER(c_char)]


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

    output = PPC_MessageQueueSize(serial_number)

    return output


PPC_Open = lib.PPC_Open
PPC_Open.restype = c_short
PPC_Open.argtypes = [POINTER(c_char)]


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

    output = PPC_Open(serial_number)

    return output


PPC_PersistSettings = lib.PPC_PersistSettings
PPC_PersistSettings.restype = c_bool
PPC_PersistSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_PersistSettings(serial_number)

    return output


PPC_PollingDuration = lib.PPC_PollingDuration
PPC_PollingDuration.restype = c_long
PPC_PollingDuration.argtypes = [POINTER(c_char)]


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

    output = PPC_PollingDuration(serial_number)

    return output


PPC_RegisterMessageCallback = lib.PPC_RegisterMessageCallback
PPC_RegisterMessageCallback.restype = c_short
PPC_RegisterMessageCallback.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_RegisterMessageCallback(serial_number)

    return output


PPC_RequestActualPosition = lib.PPC_RequestActualPosition
PPC_RequestActualPosition.restype = c_short
PPC_RequestActualPosition.argtypes = [POINTER(c_char)]


def request_actual_position(serial_number):
    '''
    Requests the position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_RequestActualPosition(serial_number)

    return output


PPC_RequestMaxOutputVoltage = lib.PPC_RequestMaxOutputVoltage
PPC_RequestMaxOutputVoltage.restype = c_bool
PPC_RequestMaxOutputVoltage.argtypes = [POINTER(c_char)]


def request_max_output_voltage(serial_number):
    '''
    Requests the maximum output voltage be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_RequestMaxOutputVoltage(serial_number)

    return output


PPC_RequestOutputVoltage = lib.PPC_RequestOutputVoltage
PPC_RequestOutputVoltage.restype = c_bool
PPC_RequestOutputVoltage.argtypes = [POINTER(c_char)]


def request_output_voltage(serial_number):
    '''
    Requests the Output Voltage be read from the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_RequestOutputVoltage(serial_number)

    return output


PPC_RequestPIDConsts = lib.PPC_RequestPIDConsts
PPC_RequestPIDConsts.restype = c_bool
PPC_RequestPIDConsts.argtypes = [POINTER(c_char)]


def request_p_i_d_consts(serial_number):
    '''
    Requests the PPC PID Constants.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_RequestPIDConsts(serial_number)

    return output


PPC_RequestPosition = lib.PPC_RequestPosition
PPC_RequestPosition.restype = c_short
PPC_RequestPosition.argtypes = [POINTER(c_char)]


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

    output = PPC_RequestPosition(serial_number)

    return output


PPC_RequestPositionControlMode = lib.PPC_RequestPositionControlMode
PPC_RequestPositionControlMode.restype = c_bool
PPC_RequestPositionControlMode.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_RequestPositionControlMode(serial_number)

    return output


PPC_RequestRackDigitalOutputs = lib.PPC_RequestRackDigitalOutputs
PPC_RequestRackDigitalOutputs.restype = c_short
PPC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]


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

    output = PPC_RequestRackDigitalOutputs(serial_number)

    return output


PPC_RequestRackStatusBits = lib.PPC_RequestRackStatusBits
PPC_RequestRackStatusBits.restype = c_short
PPC_RequestRackStatusBits.argtypes = [POINTER(c_char)]


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

    output = PPC_RequestRackStatusBits(serial_number)

    return output


PPC_RequestSettings = lib.PPC_RequestSettings
PPC_RequestSettings.restype = c_short
PPC_RequestSettings.argtypes = [POINTER(c_char)]


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

    output = PPC_RequestSettings(serial_number)

    return output


PPC_RequestStatus = lib.PPC_RequestStatus
PPC_RequestStatus.restype = c_short
PPC_RequestStatus.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_RequestStatus(serial_number)

    return output


PPC_RequestStatusBits = lib.PPC_RequestStatusBits
PPC_RequestStatusBits.restype = c_short
PPC_RequestStatusBits.argtypes = [POINTER(c_char)]


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

    output = PPC_RequestStatusBits(serial_number)

    return output


PPC_RequestVoltageSource = lib.PPC_RequestVoltageSource
PPC_RequestVoltageSource.restype = c_bool
PPC_RequestVoltageSource.argtypes = [POINTER(c_char)]


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

    output = PPC_RequestVoltageSource(serial_number)

    return output


PPC_ResetParameters = lib.PPC_ResetParameters
PPC_ResetParameters.restype = c_short
PPC_ResetParameters.argtypes = [POINTER(c_char)]


def reset_parameters(serial_number):
    '''
    Resets all parameters to power-up values.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_ResetParameters(serial_number)

    return output


PPC_SetIOSettings = lib.PPC_SetIOSettings
PPC_SetIOSettings.restype = c_short
PPC_SetIOSettings.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    ioSettings = PPC_IOSettings()

    output = PPC_SetIOSettings(serial_number)

    return output


PPC_SetMaxOutputVoltage = lib.PPC_SetMaxOutputVoltage
PPC_SetMaxOutputVoltage.restype = c_short
PPC_SetMaxOutputVoltage.argtypes = [POINTER(c_char)]


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

    output = PPC_SetMaxOutputVoltage(serial_number)

    return output


PPC_SetNotchParams = lib.PPC_SetNotchParams
PPC_SetNotchParams.restype = c_short
PPC_SetNotchParams.argtypes = [POINTER(c_char)]


def set_notch_params(serial_number):
    '''
    Sets the PPC Notch Filter Parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        notchParams: PPC_NotchParams

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    notchParams = PPC_NotchParams()

    output = PPC_SetNotchParams(serial_number)

    return output


PPC_SetOutputVoltage = lib.PPC_SetOutputVoltage
PPC_SetOutputVoltage.restype = c_short
PPC_SetOutputVoltage.argtypes = [POINTER(c_char)]


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

    output = PPC_SetOutputVoltage(serial_number)

    return output


PPC_SetPIDConsts = lib.PPC_SetPIDConsts
PPC_SetPIDConsts.restype = c_short
PPC_SetPIDConsts.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    pidConsts = PPC_PIDConsts()

    output = PPC_SetPIDConsts(serial_number)

    return output


PPC_SetPosition = lib.PPC_SetPosition
PPC_SetPosition.restype = c_short
PPC_SetPosition.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = c_short()

    output = PPC_SetPosition(serial_number)

    return output


PPC_SetPositionControlMode = lib.PPC_SetPositionControlMode
PPC_SetPositionControlMode.restype = c_short
PPC_SetPositionControlMode.argtypes = [POINTER(c_char)]


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

    output = PPC_SetPositionControlMode(serial_number)

    return output


PPC_SetPositionToTolerance = lib.PPC_SetPositionToTolerance
PPC_SetPositionToTolerance.restype = c_short
PPC_SetPositionToTolerance.argtypes = [POINTER(c_char)]


def set_position_to_tolerance(serial_number):
    '''
    Sets the position when in closed loop mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: c_short
        tolerance: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    position = c_short()
    tolerance = c_short()

    output = PPC_SetPositionToTolerance(serial_number)

    return output


PPC_SetRackDigitalOutputs = lib.PPC_SetRackDigitalOutputs
PPC_SetRackDigitalOutputs.restype = c_short
PPC_SetRackDigitalOutputs.argtypes = [POINTER(c_char)]


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

    output = PPC_SetRackDigitalOutputs(serial_number)

    return output


PPC_SetVoltageSource = lib.PPC_SetVoltageSource
PPC_SetVoltageSource.restype = c_short
PPC_SetVoltageSource.argtypes = [POINTER(c_char)]


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

    output = PPC_SetVoltageSource(serial_number)

    return output


PPC_SetZero = lib.PPC_SetZero
PPC_SetZero.restype = c_short
PPC_SetZero.argtypes = [POINTER(c_char)]


def set_zero(serial_number):
    '''
    Sets the voltage output to zero and defines the ensuing actuator position az zero.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))

    output = PPC_SetZero(serial_number)

    return output


PPC_StartPolling = lib.PPC_StartPolling
PPC_StartPolling.restype = c_bool
PPC_StartPolling.argtypes = [POINTER(c_char)]


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

    output = PPC_StartPolling(serial_number)

    return output


PPC_StopPolling = lib.PPC_StopPolling
PPC_StopPolling.restype = c_void_p
PPC_StopPolling.argtypes = [POINTER(c_char)]


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

    output = PPC_StopPolling(serial_number)

    return output


PPC_WaitForMessage = lib.PPC_WaitForMessage
PPC_WaitForMessage.restype = c_bool
PPC_WaitForMessage.argtypes = [POINTER(c_char)]


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

    serial_number = c_char_p(bytes(str(serial_number), "utf-8"))
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = PPC_WaitForMessage(serial_number)

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



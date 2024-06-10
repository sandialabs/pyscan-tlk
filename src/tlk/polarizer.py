from ctypes import (
    POINTER,
    c_bool,
    c_char,
    c_double,
    c_int,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_ulong,
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (MOT_TravelDirection, POL_PaddleBits, POL_Paddles, PolarizerParameters)
from .definitions.structures import (TLI_DeviceInfo)
from .definitions.kinesisexception import KinesisException


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Polarizer.DLL")

MPC_CheckConnection = lib.MPC_CheckConnection
MPC_CheckConnection.restype = c_bool
MPC_CheckConnection.argtypes = [POINTER(c_char)]


def check_connection(serial_number):
    # Check connection.

    serial_number = POINTER(c_char)

    output = MPC_CheckConnection(serial_number)

    return output


MPC_ClearMessageQueue = lib.MPC_ClearMessageQueue
MPC_ClearMessageQueue.restype = c_void_p
MPC_ClearMessageQueue.argtypes = [POINTER(c_char)]


def clear_message_queue(serial_number):
    # Clears the device message queue.

    serial_number = POINTER(c_char)

    output = MPC_ClearMessageQueue(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_Close = lib.MPC_Close
MPC_Close.restype = c_void_p
MPC_Close.argtypes = [POINTER(c_char)]


def close_device(serial_number):
    # Disconnect and close the device.

    serial_number = POINTER(c_char)

    output = MPC_Close(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_EnableLastMsgTimer = lib.MPC_EnableLastMsgTimer
MPC_EnableLastMsgTimer.restype = c_void_p
MPC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_bool, c_int32]


def enable_last_msg_timer(serial_number):
    # Enables the last message monitoring timer.

    serial_number = POINTER(c_char)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = MPC_EnableLastMsgTimer(serial_number, enable, lastMsgTimeout)
    if output != 0:
        raise KinesisException(output)


MPC_GetEnabledPaddles = lib.MPC_GetEnabledPaddles
MPC_GetEnabledPaddles.restype = POL_PaddleBits
MPC_GetEnabledPaddles.argtypes = [POINTER(c_char)]


def get_enabled_paddles(serial_number):
    # Gets enabled paddles.

    serial_number = POINTER(c_char)

    output = MPC_GetEnabledPaddles(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_GetFirmwareVersion = lib.MPC_GetFirmwareVersion
MPC_GetFirmwareVersion.restype = c_ulong
MPC_GetFirmwareVersion.argtypes = [POINTER(c_char)]


def get_firmware_version(serial_number):
    # Gets version number of firmware.

    serial_number = POINTER(c_char)

    output = MPC_GetFirmwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_GetHardwareInfo = lib.MPC_GetHardwareInfo
MPC_GetHardwareInfo.restype = c_short
MPC_GetHardwareInfo.argtypes = [
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
    numchannels = c_long()
    notes = POINTER(c_char)
    sizeOfNotes = c_ulong()
    firmwareVersion = c_ulong()
    hardwareVersion = c_long()
    modificationState = c_long()

    output = MPC_GetHardwareInfo(
        serial_number,
        modelNo,
        sizeOfModelNo,
        type,
        numchannels,
        notes,
        sizeOfNotes,
        firmwareVersion,
        hardwareVersion,
        modificationState)
    if output != 0:
        raise KinesisException(output)


MPC_GetHomeOffset = lib.MPC_GetHomeOffset
MPC_GetHomeOffset.restype = c_double
MPC_GetHomeOffset.argtypes = [POINTER(c_char)]


def get_home_offset(serial_number):
    # Gets home offset.

    serial_number = POINTER(c_char)

    output = MPC_GetHomeOffset(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_GetJogSize = lib.MPC_GetJogSize
MPC_GetJogSize.restype = c_double
MPC_GetJogSize.argtypes = [POINTER(c_char), POL_Paddles]


def get_jog_size(serial_number):
    # Gets step size.

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()

    output = MPC_GetJogSize(serial_number, paddle)
    if output != 0:
        raise KinesisException(output)


MPC_GetMaxTravel = lib.MPC_GetMaxTravel
MPC_GetMaxTravel.restype = c_double
MPC_GetMaxTravel.argtypes = [POINTER(c_char)]


def get_max_travel(serial_number):
    # Get the maximum travel in encoder steps.

    serial_number = POINTER(c_char)

    output = MPC_GetMaxTravel(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_GetNextMessage = lib.MPC_GetNextMessage
MPC_GetNextMessage.restype = c_bool
MPC_GetNextMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def get_next_message(serial_number):
    # Get the next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = MPC_GetNextMessage(serial_number, messageType, messageID, messageData)

    return output


MPC_GetPaddleCount = lib.MPC_GetPaddleCount
MPC_GetPaddleCount.restype = c_int
MPC_GetPaddleCount.argtypes = [POINTER(c_char)]


def get_paddle_count(serial_number):
    # Get number of polarizer paddles.

    serial_number = POINTER(c_char)

    output = MPC_GetPaddleCount(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_GetPolParams = lib.MPC_GetPolParams
MPC_GetPolParams.restype = c_short
MPC_GetPolParams.argtypes = [POINTER(c_char), PolarizerParameters]


def get_pol_params(serial_number):
    # Gets the polarizer parameters.

    serial_number = POINTER(c_char)
    polParams = PolarizerParameters()

    output = MPC_GetPolParams(serial_number, polParams)
    if output != 0:
        raise KinesisException(output)


MPC_GetPosition = lib.MPC_GetPosition
MPC_GetPosition.restype = c_double
MPC_GetPosition.argtypes = [POINTER(c_char), POL_Paddles]


def get_position(serial_number):
    # Get the current position.

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()

    output = MPC_GetPosition(serial_number, paddle)
    if output != 0:
        raise KinesisException(output)


MPC_GetSoftwareVersion = lib.MPC_GetSoftwareVersion
MPC_GetSoftwareVersion.restype = c_ulong
MPC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


def get_software_version(serial_number):
    # Gets version number of the device software.

    serial_number = POINTER(c_char)

    output = MPC_GetSoftwareVersion(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_GetStatusBits = lib.MPC_GetStatusBits
MPC_GetStatusBits.restype = c_ulong
MPC_GetStatusBits.argtypes = [POINTER(c_char), POL_Paddles]


def get_status_bits(serial_number):
    # Get the current status bits.

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()

    output = MPC_GetStatusBits(serial_number, paddle)
    if output != 0:
        raise KinesisException(output)


MPC_GetStepsPerDegree = lib.MPC_GetStepsPerDegree
MPC_GetStepsPerDegree.restype = c_double
MPC_GetStepsPerDegree.argtypes = [POINTER(c_char)]


def get_steps_per_degree(serial_number):
    # Get the Ratio of encoder steps per degree.

    serial_number = POINTER(c_char)

    output = MPC_GetStepsPerDegree(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_GetVelocity = lib.MPC_GetVelocity
MPC_GetVelocity.restype = c_short
MPC_GetVelocity.argtypes = [POINTER(c_char)]


def get_velocity(serial_number):
    # Gets the velocity.

    serial_number = POINTER(c_char)

    output = MPC_GetVelocity(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_HasLastMsgTimerOverrun = lib.MPC_HasLastMsgTimerOverrun
MPC_HasLastMsgTimerOverrun.restype = c_bool
MPC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char)]


def has_last_msg_timer_overrun(serial_number):
    # Queries if the time since the last message has exceeded the
    # lastMsgTimeout set by MPC_EnableLastMsgTimer(char const * serialNo, bool
    # enable, __int32 lastMsgTimeout ).

    serial_number = POINTER(c_char)

    output = MPC_HasLastMsgTimerOverrun(serial_number)

    return output


MPC_Home = lib.MPC_Home
MPC_Home.restype = c_short
MPC_Home.argtypes = [POINTER(c_char), POL_Paddles]


def home(serial_number):
    # Home the device.

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()

    output = MPC_Home(serial_number, paddle)
    if output != 0:
        raise KinesisException(output)


MPC_Identify = lib.MPC_Identify
MPC_Identify.restype = c_void_p
MPC_Identify.argtypes = [POINTER(c_char)]


def identify(serial_number):
    # Sends a command to the device to make it identify iteself.

    serial_number = POINTER(c_char)

    output = MPC_Identify(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_IsPaddleEnabled = lib.MPC_IsPaddleEnabled
MPC_IsPaddleEnabled.restype = c_bool
MPC_IsPaddleEnabled.argtypes = [POINTER(c_char), POL_Paddles]


def is_paddle_enabled(serial_number):
    # Queries if a paddle is enabled.

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()

    output = MPC_IsPaddleEnabled(serial_number, paddle)

    return output


MPC_Jog = lib.MPC_Jog
MPC_Jog.restype = c_short
MPC_Jog.argtypes = [POINTER(c_char), POL_Paddles, MOT_TravelDirection]


def jog(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()
    direction = MOT_TravelDirection()

    output = MPC_Jog(serial_number, paddle, direction)
    if output != 0:
        raise KinesisException(output)


MPC_LoadNamedSettings = lib.MPC_LoadNamedSettings
MPC_LoadNamedSettings.restype = c_bool
MPC_LoadNamedSettings.argtypes = [POINTER(c_char), POINTER(c_char)]


def load_named_settings(serial_number):
    # Update device with named settings.

    serial_number = POINTER(c_char)
    settingsName = POINTER(c_char)

    output = MPC_LoadNamedSettings(serial_number, settingsName)

    return output


MPC_LoadSettings = lib.MPC_LoadSettings
MPC_LoadSettings.restype = c_bool
MPC_LoadSettings.argtypes = [POINTER(c_char)]


def load_settings(serial_number):
    # Update device with stored settings.

    serial_number = POINTER(c_char)

    output = MPC_LoadSettings(serial_number)

    return output


MPC_MessageQueueSize = lib.MPC_MessageQueueSize
MPC_MessageQueueSize.restype = c_int
MPC_MessageQueueSize.argtypes = [POINTER(c_char)]


def message_queue_size(serial_number):
    # Gets the MessageQueue size.

    serial_number = POINTER(c_char)

    output = MPC_MessageQueueSize(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_MoveRelative = lib.MPC_MoveRelative
MPC_MoveRelative.restype = c_short
MPC_MoveRelative.argtypes = [POINTER(c_char), POL_Paddles, c_double]


def move_relative(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()
    position = c_double()

    output = MPC_MoveRelative(serial_number, paddle, position)
    if output != 0:
        raise KinesisException(output)


MPC_MoveToPosition = lib.MPC_MoveToPosition
MPC_MoveToPosition.restype = c_short
MPC_MoveToPosition.argtypes = [POINTER(c_char), POL_Paddles, c_double]


def move_to_position(serial_number):
    # Move the device to the specified position (index).

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()
    position = c_double()

    output = MPC_MoveToPosition(serial_number, paddle, position)
    if output != 0:
        raise KinesisException(output)


MPC_Open = lib.MPC_Open
MPC_Open.restype = c_short
MPC_Open.argtypes = [POINTER(c_char)]


def open_device(serial_number):
    # Open the device for communications.

    serial_number = POINTER(c_char)

    output = MPC_Open(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_PersistSettings = lib.MPC_PersistSettings
MPC_PersistSettings.restype = c_bool
MPC_PersistSettings.argtypes = [POINTER(c_char)]


def persist_settings(serial_number):
    # Persist the devices current settings.

    serial_number = POINTER(c_char)

    output = MPC_PersistSettings(serial_number)

    return output


MPC_PollingDuration = lib.MPC_PollingDuration
MPC_PollingDuration.restype = c_long
MPC_PollingDuration.argtypes = [POINTER(c_char)]


def polling_duration(serial_number):
    # Gets the polling loop duration.

    serial_number = POINTER(c_char)

    output = MPC_PollingDuration(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_RegisterMessageCallback = lib.MPC_RegisterMessageCallback
MPC_RegisterMessageCallback.restype = c_void_p
MPC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_void_p]


def register_message_callback(serial_number):
    # Registers a callback on the message queue.

    serial_number = POINTER(c_char)
    void = c_void_p()

    output = MPC_RegisterMessageCallback(serial_number, void)
    if output != 0:
        raise KinesisException(output)


MPC_RequestPolParams = lib.MPC_RequestPolParams
MPC_RequestPolParams.restype = c_short
MPC_RequestPolParams.argtypes = [POINTER(c_char)]


def request_pol_params(serial_number):
    # Request polarizer parameters.

    serial_number = POINTER(c_char)

    output = MPC_RequestPolParams(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_RequestSettings = lib.MPC_RequestSettings
MPC_RequestSettings.restype = c_short
MPC_RequestSettings.argtypes = [POINTER(c_char)]


def request_settings(serial_number):
    # Requests that all settings are download from device.

    serial_number = POINTER(c_char)

    output = MPC_RequestSettings(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_RequestStatus = lib.MPC_RequestStatus
MPC_RequestStatus.restype = c_short
MPC_RequestStatus.argtypes = [POINTER(c_char)]


def request_status(serial_number):
    # Request status bits.

    serial_number = POINTER(c_char)

    output = MPC_RequestStatus(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_ResetParameters = lib.MPC_ResetParameters
MPC_ResetParameters.restype = c_bool
MPC_ResetParameters.argtypes = [POINTER(c_char)]


def reset_parameters(serial_number):
    # Mpc reset parameters.

    serial_number = POINTER(c_char)

    output = MPC_ResetParameters(serial_number)

    return output


MPC_SetEnabledPaddles = lib.MPC_SetEnabledPaddles
MPC_SetEnabledPaddles.restype = c_int
MPC_SetEnabledPaddles.argtypes = [POINTER(c_char), POL_PaddleBits]


def set_enabled_paddles(serial_number):
    # Enables the specified paddles.

    serial_number = POINTER(c_char)
    paddles = POL_PaddleBits()

    output = MPC_SetEnabledPaddles(serial_number, paddles)
    if output != 0:
        raise KinesisException(output)


MPC_SetHomeOffset = lib.MPC_SetHomeOffset
MPC_SetHomeOffset.restype = c_short
MPC_SetHomeOffset.argtypes = [POINTER(c_char), c_double]


def set_home_offset(serial_number):
    # Sets home offset.

    serial_number = POINTER(c_char)
    homeOffset = c_double()

    output = MPC_SetHomeOffset(serial_number, homeOffset)
    if output != 0:
        raise KinesisException(output)


MPC_SetJogSize = lib.MPC_SetJogSize
MPC_SetJogSize.restype = c_short
MPC_SetJogSize.argtypes = [POINTER(c_char), POL_Paddles, c_double]


def set_jog_size(serial_number):
    # Sets jog size.

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()
    jogSize = c_double()

    output = MPC_SetJogSize(serial_number, paddle, jogSize)
    if output != 0:
        raise KinesisException(output)


MPC_SetPolParams = lib.MPC_SetPolParams
MPC_SetPolParams.restype = c_short
MPC_SetPolParams.argtypes = [POINTER(c_char), PolarizerParameters]


def set_pol_params(serial_number):
    # Gets the polarizer parameters.

    serial_number = POINTER(c_char)
    polParams = PolarizerParameters()

    output = MPC_SetPolParams(serial_number, polParams)
    if output != 0:
        raise KinesisException(output)


MPC_SetVelocity = lib.MPC_SetVelocity
MPC_SetVelocity.restype = c_short
MPC_SetVelocity.argtypes = [POINTER(c_char), c_short]


def set_velocity(serial_number):
    # Sets a velocity.

    serial_number = POINTER(c_char)
    velocity = c_short()

    output = MPC_SetVelocity(serial_number, velocity)
    if output != 0:
        raise KinesisException(output)


MPC_StartPolling = lib.MPC_StartPolling
MPC_StartPolling.restype = c_bool
MPC_StartPolling.argtypes = [POINTER(c_char), c_int]


def start_polling(serial_number):
    # Starts the internal polling loop which continuously requests position and status.

    serial_number = POINTER(c_char)
    milliseconds = c_int()

    output = MPC_StartPolling(serial_number, milliseconds)

    return output


MPC_Stop = lib.MPC_Stop
MPC_Stop.restype = c_short
MPC_Stop.argtypes = [POINTER(c_char), POL_Paddles]


def stop(serial_number):
    # Stop the device .

    serial_number = POINTER(c_char)
    paddle = POL_Paddles()

    output = MPC_Stop(serial_number, paddle)
    if output != 0:
        raise KinesisException(output)


MPC_StopPolling = lib.MPC_StopPolling
MPC_StopPolling.restype = c_void_p
MPC_StopPolling.argtypes = [POINTER(c_char)]


def stop_polling(serial_number):
    # Stops the internal polling loop.

    serial_number = POINTER(c_char)

    output = MPC_StopPolling(serial_number)
    if output != 0:
        raise KinesisException(output)


MPC_TimeSinceLastMsgReceived = lib.MPC_TimeSinceLastMsgReceived
MPC_TimeSinceLastMsgReceived.restype = c_bool
MPC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_int64]


def time_since_last_msg_received(serial_number):
    # Gets the time in milliseconds since tha last message was received from the device.

    serial_number = POINTER(c_char)
    lastUpdateTimeMS = c_int64()

    output = MPC_TimeSinceLastMsgReceived(serial_number, lastUpdateTimeMS)

    return output


MPC_WaitForMessage = lib.MPC_WaitForMessage
MPC_WaitForMessage.restype = c_bool
MPC_WaitForMessage.argtypes = [POINTER(c_char), c_long, c_long, c_ulong]


def wait_for_message(serial_number):
    # Wait for next MessageQueue item.

    serial_number = POINTER(c_char)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = MPC_WaitForMessage(serial_number, messageType, messageID, messageData)

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

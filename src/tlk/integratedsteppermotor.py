from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_char_p,
    c_double,
    c_float,
    c_int,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    c_void_p,
    cdll,
    pointer)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    MOT_ButtonModes,
    MOT_JogModes,
    MOT_LimitSwitchModes,
    MOT_LimitSwitchSWModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes)
from .definitions.structures import (
    MOT_ButtonParameters,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_LimitSwitchParameters,
    MOT_PotentiometerSteps,
    MOT_PowerParameters,
    MOT_VelocityParameters,
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
    lib_path + "Thorlabs.MotionControl.IntegratedStepperMotors.DLL")

ISC_CanHome = lib.ISC_CanHome
ISC_CanHome.restype = c_bool
ISC_CanHome.argtypes = []


def can_home(serial_number):
    '''
    Can the device perform a Home.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_CanHome(serial_number)

    return output


ISC_CanMoveWithoutHomingFirst = lib.ISC_CanMoveWithoutHomingFirst
ISC_CanMoveWithoutHomingFirst.restype = c_bool
ISC_CanMoveWithoutHomingFirst.argtypes = []


def can_move_without_homing_first(serial_number):
    '''
    Can this device be moved without Homing.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_CanMoveWithoutHomingFirst(serial_number)

    return output


ISC_CheckConnection = lib.ISC_CheckConnection
ISC_CheckConnection.restype = c_bool
ISC_CheckConnection.argtypes = [POINTER(c_char)]


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

    output = ISC_CheckConnection(serial_number)

    return output


ISC_ClearMessageQueue = lib.ISC_ClearMessageQueue
ISC_ClearMessageQueue.restype = c_void_p
ISC_ClearMessageQueue.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = ISC_ClearMessageQueue(serial_number)

    return output


ISC_Close = lib.ISC_Close
ISC_Close.restype = c_void_p
ISC_Close.argtypes = []


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

    output = ISC_Close(serial_number)

    return output


ISC_DisableChannel = lib.ISC_DisableChannel
ISC_DisableChannel.restype = c_short
ISC_DisableChannel.argtypes = []


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

    output = ISC_DisableChannel(serial_number)

    return output


ISC_EnableChannel = lib.ISC_EnableChannel
ISC_EnableChannel.restype = c_short
ISC_EnableChannel.argtypes = []


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

    output = ISC_EnableChannel(serial_number)

    return output


ISC_EnableLastMsgTimer = lib.ISC_EnableLastMsgTimer
ISC_EnableLastMsgTimer.restype = c_void_p
ISC_EnableLastMsgTimer.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    enable = c_bool()
    lastMsgTimeout = c_int32()

    output = ISC_EnableLastMsgTimer(serial_number)

    return output


ISC_GetBacklash = lib.ISC_GetBacklash
ISC_GetBacklash.restype = c_long
ISC_GetBacklash.argtypes = []


def get_backlash(serial_number):
    '''
    Get the backlash distance setting (used to control hysteresis).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetBacklash(serial_number)

    return output


ISC_GetBowIndex = lib.ISC_GetBowIndex
ISC_GetBowIndex.restype = c_short
ISC_GetBowIndex.argtypes = []


def get_bow_index(serial_number):
    '''
    Gets the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetBowIndex(serial_number)

    return output


ISC_GetButtonParams = lib.ISC_GetButtonParams
ISC_GetButtonParams.restype = c_short
ISC_GetButtonParams.argtypes = []


def get_button_params(serial_number):
    '''
    Gets the LTS button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonMode: MOT_ButtonModes
        leftButtonPosition: c_int
        rightButtonPosition: c_int
        timeout: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()
    timeout = c_short()

    output = ISC_GetButtonParams(serial_number)

    return output


ISC_GetButtonParamsBlock = lib.ISC_GetButtonParamsBlock
ISC_GetButtonParamsBlock.restype = c_short
ISC_GetButtonParamsBlock.argtypes = []


def get_button_params_block(serial_number):
    '''
    Get the button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonParams: MOT_ButtonParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonParams = MOT_ButtonParameters()

    output = ISC_GetButtonParamsBlock(serial_number)

    return output


ISC_GetCalibrationFile = lib.ISC_GetCalibrationFile
ISC_GetCalibrationFile.restype = c_bool
ISC_GetCalibrationFile.argtypes = []


def get_calibration_file(serial_number):
    '''
    Get calibration file for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        filename: POINTER(c_char)
        sizeOfBuffer: c_short

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)
    filename = POINTER(c_char)()
    sizeOfBuffer = c_short()

    output = ISC_GetCalibrationFile(serial_number)

    return output


ISC_GetDeviceUnitFromRealValue = lib.ISC_GetDeviceUnitFromRealValue
ISC_GetDeviceUnitFromRealValue.restype = c_short
ISC_GetDeviceUnitFromRealValue.argtypes = []


def get_device_unit_from_real_value(serial_number):
    '''
    Converts a device unit to a real world unit.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        real_unit: c_double
        device_unit: c_int
        unitType: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    real_unit = c_double()
    device_unit = c_int()
    unitType = c_int()

    output = ISC_GetDeviceUnitFromRealValue(serial_number)

    return output


ISC_GetFirmwareVersion = lib.ISC_GetFirmwareVersion
ISC_GetFirmwareVersion.restype = c_ulong
ISC_GetFirmwareVersion.argtypes = []


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

    output = ISC_GetFirmwareVersion(serial_number)

    return output


ISC_GetHardwareInfo = lib.ISC_GetHardwareInfo
ISC_GetHardwareInfo.restype = c_short
ISC_GetHardwareInfo.argtypes = [POINTER(c_char)]


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

    output = ISC_GetHardwareInfo(serial_number)

    return output


ISC_GetHardwareInfoBlock = lib.ISC_GetHardwareInfoBlock
ISC_GetHardwareInfoBlock.restype = c_short
ISC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


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

    output = ISC_GetHardwareInfoBlock(serial_number)

    return output


ISC_GetHomingParamsBlock = lib.ISC_GetHomingParamsBlock
ISC_GetHomingParamsBlock.restype = c_short
ISC_GetHomingParamsBlock.argtypes = []


def get_homing_params_block(serial_number):
    '''
    Get the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        homingParams: MOT_HomingParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    homingParams = MOT_HomingParameters()

    output = ISC_GetHomingParamsBlock(serial_number)

    return output


ISC_GetHomingVelocity = lib.ISC_GetHomingVelocity
ISC_GetHomingVelocity.restype = c_uint
ISC_GetHomingVelocity.argtypes = []


def get_homing_velocity(serial_number):
    '''
    Gets the homing velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_uint
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetHomingVelocity(serial_number)

    return output


ISC_GetJogMode = lib.ISC_GetJogMode
ISC_GetJogMode.restype = c_short
ISC_GetJogMode.argtypes = []


def get_jog_mode(serial_number):
    '''
    Gets the jog mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: MOT_JogModes
        stopMode: MOT_StopModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = ISC_GetJogMode(serial_number)

    return output


ISC_GetJogParamsBlock = lib.ISC_GetJogParamsBlock
ISC_GetJogParamsBlock.restype = c_short
ISC_GetJogParamsBlock.argtypes = []


def get_jog_params_block(serial_number):
    '''
    Get the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        jogParams: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    jogParams = MOT_JogParameters()

    output = ISC_GetJogParamsBlock(serial_number)

    return output


ISC_GetJogStepSize = lib.ISC_GetJogStepSize
ISC_GetJogStepSize.restype = c_uint
ISC_GetJogStepSize.argtypes = []


def get_jog_step_size(serial_number):
    '''
    Gets the distance to move when jogging.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_uint
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetJogStepSize(serial_number)

    return output


ISC_GetJogVelParams = lib.ISC_GetJogVelParams
ISC_GetJogVelParams.restype = c_short
ISC_GetJogVelParams.argtypes = []


def get_jog_vel_params(serial_number):
    '''
    Gets the jog velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_GetJogVelParams(serial_number)

    return output


ISC_GetLEDswitches = lib.ISC_GetLEDswitches
ISC_GetLEDswitches.restype = c_long
ISC_GetLEDswitches.argtypes = []


def get_l_e_dswitches(serial_number):
    '''
    Get the LED indicator bits on device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetLEDswitches(serial_number)

    return output


ISC_GetLimitSwitchParams = lib.ISC_GetLimitSwitchParams
ISC_GetLimitSwitchParams.restype = c_short
ISC_GetLimitSwitchParams.argtypes = []


def get_limit_switch_params(serial_number):
    '''
    Gets the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        clockwiseHardwareLimit: MOT_LimitSwitchModes
        anticlockwiseHardwareLimit: MOT_LimitSwitchModes
        clockwisePosition: c_uint
        anticlockwisePosition: c_uint
        softLimitMode: MOT_LimitSwitchSWModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = ISC_GetLimitSwitchParams(serial_number)

    return output


ISC_GetLimitSwitchParamsBlock = lib.ISC_GetLimitSwitchParamsBlock
ISC_GetLimitSwitchParamsBlock.restype = c_short
ISC_GetLimitSwitchParamsBlock.argtypes = []


def get_limit_switch_params_block(serial_number):
    '''
    Get the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        limitSwitchParams: MOT_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = ISC_GetLimitSwitchParamsBlock(serial_number)

    return output


ISC_GetMotorParams = lib.ISC_GetMotorParams
ISC_GetMotorParams.restype = c_short
ISC_GetMotorParams.argtypes = []


def get_motor_params(serial_number):
    '''
    Gets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_long
        gearBoxRatio: c_long
        pitch: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = ISC_GetMotorParams(serial_number)

    return output


ISC_GetMotorParamsExt = lib.ISC_GetMotorParamsExt
ISC_GetMotorParamsExt.restype = c_short
ISC_GetMotorParamsExt.argtypes = []


def get_motor_params_ext(serial_number):
    '''
    Gets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_double
        gearBoxRatio: c_double
        pitch: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = ISC_GetMotorParamsExt(serial_number)

    return output


ISC_GetMotorTravelLimits = lib.ISC_GetMotorTravelLimits
ISC_GetMotorTravelLimits.restype = c_short
ISC_GetMotorTravelLimits.argtypes = []


def get_motor_travel_limits(serial_number):
    '''
    Gets the absolute minimum and maximum travel range constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        minPosition: c_double
        maxPosition: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    minPosition = c_double()
    maxPosition = c_double()

    output = ISC_GetMotorTravelLimits(serial_number)

    return output


ISC_GetMotorTravelMode = lib.ISC_GetMotorTravelMode
ISC_GetMotorTravelMode.restype = MOT_TravelModes
ISC_GetMotorTravelMode.argtypes = []


def get_motor_travel_mode(serial_number):
    '''
    Get the motor travel mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        MOT_TravelModes
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetMotorTravelMode(serial_number)

    return output


ISC_GetMotorVelocityLimits = lib.ISC_GetMotorVelocityLimits
ISC_GetMotorVelocityLimits.restype = c_short
ISC_GetMotorVelocityLimits.argtypes = []


def get_motor_velocity_limits(serial_number):
    '''
    Gets the absolute maximum velocity and acceleration constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        maxVelocity: c_double
        maxAcceleration: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = ISC_GetMotorVelocityLimits(serial_number)

    return output


ISC_GetMoveAbsolutePosition = lib.ISC_GetMoveAbsolutePosition
ISC_GetMoveAbsolutePosition.restype = c_int
ISC_GetMoveAbsolutePosition.argtypes = []


def get_move_absolute_position(serial_number):
    '''
    Gets the move absolute position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetMoveAbsolutePosition(serial_number)

    return output


ISC_GetMoveRelativeDistance = lib.ISC_GetMoveRelativeDistance
ISC_GetMoveRelativeDistance.restype = c_int
ISC_GetMoveRelativeDistance.argtypes = []


def get_move_relative_distance(serial_number):
    '''
    Gets the move relative distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetMoveRelativeDistance(serial_number)

    return output


ISC_GetNextMessage = lib.ISC_GetNextMessage
ISC_GetNextMessage.restype = c_bool
ISC_GetNextMessage.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = ISC_GetNextMessage(serial_number)

    return output


ISC_GetNumberPositions = lib.ISC_GetNumberPositions
ISC_GetNumberPositions.restype = c_int
ISC_GetNumberPositions.argtypes = []


def get_number_positions(serial_number):
    '''
    Get number of positions.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetNumberPositions(serial_number)

    return output


ISC_GetPosition = lib.ISC_GetPosition
ISC_GetPosition.restype = c_int
ISC_GetPosition.argtypes = []


def get_position(serial_number):
    '''
    Get the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetPosition(serial_number)

    return output


ISC_GetPositionCounter = lib.ISC_GetPositionCounter
ISC_GetPositionCounter.restype = c_long
ISC_GetPositionCounter.argtypes = []


def get_position_counter(serial_number):
    '''
    Get the Position Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_long
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetPositionCounter(serial_number)

    return output


ISC_GetPotentiometerParams = lib.ISC_GetPotentiometerParams
ISC_GetPotentiometerParams.restype = c_short
ISC_GetPotentiometerParams.argtypes = []


def get_potentiometer_params(serial_number):
    '''
    Gets the potentiometer parameters for the LTS.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_short
        thresholdDeflection: c_long
        velocity: c_ulong

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = ISC_GetPotentiometerParams(serial_number)

    return output


ISC_GetPotentiometerParamsBlock = lib.ISC_GetPotentiometerParamsBlock
ISC_GetPotentiometerParamsBlock.restype = c_short
ISC_GetPotentiometerParamsBlock.argtypes = []


def get_potentiometer_params_block(serial_number):
    '''
    Get the potentiometer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        potentiometerSteps: MOT_PotentiometerSteps

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = ISC_GetPotentiometerParamsBlock(serial_number)

    return output


ISC_GetPowerParams = lib.ISC_GetPowerParams
ISC_GetPowerParams.restype = c_short
ISC_GetPowerParams.argtypes = []


def get_power_params(serial_number):
    '''
    Gets the power parameters for the stepper motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        powerParams: MOT_PowerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    powerParams = MOT_PowerParameters()

    output = ISC_GetPowerParams(serial_number)

    return output


ISC_GetRealValueFromDeviceUnit = lib.ISC_GetRealValueFromDeviceUnit
ISC_GetRealValueFromDeviceUnit.restype = c_short
ISC_GetRealValueFromDeviceUnit.argtypes = []


def get_real_value_from_device_unit(serial_number):
    '''
    Converts a device unit to a real world unit.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        device_unit: c_int
        real_unit: c_double
        unitType: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    device_unit = c_int()
    real_unit = c_double()
    unitType = c_int()

    output = ISC_GetRealValueFromDeviceUnit(serial_number)

    return output


ISC_GetSoftLimitMode = lib.ISC_GetSoftLimitMode
ISC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
ISC_GetSoftLimitMode.argtypes = []


def get_soft_limit_mode(serial_number):
    '''
    Gets the software limits mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        MOT_LimitsSoftwareApproachPolicy
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetSoftLimitMode(serial_number)

    return output


ISC_GetSoftwareVersion = lib.ISC_GetSoftwareVersion
ISC_GetSoftwareVersion.restype = c_ulong
ISC_GetSoftwareVersion.argtypes = []


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

    output = ISC_GetSoftwareVersion(serial_number)

    return output


ISC_GetStageAxisMaxPos = lib.ISC_GetStageAxisMaxPos
ISC_GetStageAxisMaxPos.restype = c_int
ISC_GetStageAxisMaxPos.argtypes = []


def get_stage_axis_max_pos(serial_number):
    '''
    Gets the LTS Motor maximum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetStageAxisMaxPos(serial_number)

    return output


ISC_GetStageAxisMinPos = lib.ISC_GetStageAxisMinPos
ISC_GetStageAxisMinPos.restype = c_int
ISC_GetStageAxisMinPos.argtypes = []


def get_stage_axis_min_pos(serial_number):
    '''
    Gets the LTS Motor minimum stage position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_int
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetStageAxisMinPos(serial_number)

    return output


ISC_GetStatusBits = lib.ISC_GetStatusBits
ISC_GetStatusBits.restype = c_ulong
ISC_GetStatusBits.argtypes = []


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

    output = ISC_GetStatusBits(serial_number)

    return output


ISC_GetTriggerSwitches = lib.ISC_GetTriggerSwitches
ISC_GetTriggerSwitches.restype = c_byte
ISC_GetTriggerSwitches.argtypes = []


def get_trigger_switches(serial_number):
    '''
    Gets the trigger switch bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_byte
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_GetTriggerSwitches(serial_number)

    return output


ISC_GetVelParams = lib.ISC_GetVelParams
ISC_GetVelParams.restype = c_short
ISC_GetVelParams.argtypes = []


def get_vel_params(serial_number):
    '''
    Gets the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_GetVelParams(serial_number)

    return output


ISC_GetVelParamsBlock = lib.ISC_GetVelParamsBlock
ISC_GetVelParamsBlock.restype = c_short
ISC_GetVelParamsBlock.argtypes = []


def get_vel_params_block(serial_number):
    '''
    Get the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        velocityParams: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    velocityParams = MOT_VelocityParameters()

    output = ISC_GetVelParamsBlock(serial_number)

    return output


ISC_HasLastMsgTimerOverrun = lib.ISC_HasLastMsgTimerOverrun
ISC_HasLastMsgTimerOverrun.restype = c_bool
ISC_HasLastMsgTimerOverrun.argtypes = []


def has_last_msg_timer_overrun(serial_number):
    '''
    Queries if the time since the last message has exceeded the lastMsgTimeout set by ISC_EnableLastMsgTimer(char const * serialNo, bool enable, __int32 lastMsgTimeout ).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_HasLastMsgTimerOverrun(serial_number)

    return output


ISC_Home = lib.ISC_Home
ISC_Home.restype = c_short
ISC_Home.argtypes = []


def home(serial_number):
    '''
    Home the device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_Home(serial_number)

    return output


ISC_Identify = lib.ISC_Identify
ISC_Identify.restype = c_void_p
ISC_Identify.argtypes = []


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

    output = ISC_Identify(serial_number)

    return output


ISC_IsCalibrationActive = lib.ISC_IsCalibrationActive
ISC_IsCalibrationActive.restype = c_bool
ISC_IsCalibrationActive.argtypes = []


def is_calibration_active(serial_number):
    '''
    Is a calibration file active for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_IsCalibrationActive(serial_number)

    return output


ISC_LoadNamedSettings = lib.ISC_LoadNamedSettings
ISC_LoadNamedSettings.restype = c_bool
ISC_LoadNamedSettings.argtypes = []


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

    output = ISC_LoadNamedSettings(serial_number)

    return output


ISC_LoadSettings = lib.ISC_LoadSettings
ISC_LoadSettings.restype = c_bool
ISC_LoadSettings.argtypes = []


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

    output = ISC_LoadSettings(serial_number)

    return output


ISC_MessageQueueSize = lib.ISC_MessageQueueSize
ISC_MessageQueueSize.restype = c_int
ISC_MessageQueueSize.argtypes = []


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

    output = ISC_MessageQueueSize(serial_number)

    return output


ISC_MoveAbsolute = lib.ISC_MoveAbsolute
ISC_MoveAbsolute.restype = c_short
ISC_MoveAbsolute.argtypes = []


def move_absolute(serial_number):
    '''
    Moves the device to the position defined in the SetMoveAbsolute command.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_MoveAbsolute(serial_number)

    return output


ISC_MoveAtVelocity = lib.ISC_MoveAtVelocity
ISC_MoveAtVelocity.restype = c_short
ISC_MoveAtVelocity.argtypes = []


def move_at_velocity(serial_number):
    '''
    Start moving at the current velocity in the specified direction.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        direction: MOT_TravelDirection

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    direction = MOT_TravelDirection()

    output = ISC_MoveAtVelocity(serial_number)

    return output


ISC_MoveJog = lib.ISC_MoveJog
ISC_MoveJog.restype = c_short
ISC_MoveJog.argtypes = []


def move_jog(serial_number):
    '''
    Perform a jog.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        jogDirection: MOT_TravelDirection

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    jogDirection = MOT_TravelDirection()

    output = ISC_MoveJog(serial_number)

    return output


ISC_MoveRelative = lib.ISC_MoveRelative
ISC_MoveRelative.restype = c_short
ISC_MoveRelative.argtypes = []


def move_relative(serial_number):
    '''
    Move the motor by a relative amount.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        displacement: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    displacement = c_int()

    output = ISC_MoveRelative(serial_number)

    return output


ISC_MoveRelativeDistance = lib.ISC_MoveRelativeDistance
ISC_MoveRelativeDistance.restype = c_short
ISC_MoveRelativeDistance.argtypes = []


def move_relative_distance(serial_number):
    '''
    Moves the device by a relative distancce defined by SetMoveRelativeDistance.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_MoveRelativeDistance(serial_number)

    return output


ISC_MoveToPosition = lib.ISC_MoveToPosition
ISC_MoveToPosition.restype = c_short
ISC_MoveToPosition.argtypes = []


def move_to_position(serial_number):
    '''
    Move the device to the specified position (index).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_int()

    output = ISC_MoveToPosition(serial_number)

    return output


ISC_NeedsHoming = lib.ISC_NeedsHoming
ISC_NeedsHoming.restype = c_bool
ISC_NeedsHoming.argtypes = []


def needs_homing(serial_number):
    '''
    Does the device need to be Homed before a move can be performed.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_bool
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_NeedsHoming(serial_number)

    return output


ISC_Open = lib.ISC_Open
ISC_Open.restype = c_short
ISC_Open.argtypes = []


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

    output = ISC_Open(serial_number)

    return output


ISC_PersistSettings = lib.ISC_PersistSettings
ISC_PersistSettings.restype = c_bool
ISC_PersistSettings.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = ISC_PersistSettings(serial_number)

    return output


ISC_PollingDuration = lib.ISC_PollingDuration
ISC_PollingDuration.restype = c_long
ISC_PollingDuration.argtypes = []


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

    output = ISC_PollingDuration(serial_number)

    return output


ISC_RegisterMessageCallback = lib.ISC_RegisterMessageCallback
ISC_RegisterMessageCallback.restype = c_void_p
ISC_RegisterMessageCallback.argtypes = []


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

    serial_number = c_char_pointer(serial_number)

    output = ISC_RegisterMessageCallback(serial_number)

    return output


ISC_RequestBacklash = lib.ISC_RequestBacklash
ISC_RequestBacklash.restype = c_short
ISC_RequestBacklash.argtypes = []


def request_backlash(serial_number):
    '''
    Requests the backlash.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestBacklash(serial_number)

    return output


ISC_RequestBowIndex = lib.ISC_RequestBowIndex
ISC_RequestBowIndex.restype = c_short
ISC_RequestBowIndex.argtypes = []


def request_bow_index(serial_number):
    '''
    Requests the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestBowIndex(serial_number)

    return output


ISC_RequestButtonParams = lib.ISC_RequestButtonParams
ISC_RequestButtonParams.restype = c_short
ISC_RequestButtonParams.argtypes = []


def request_button_params(serial_number):
    '''
    Requests the LTS button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestButtonParams(serial_number)

    return output


ISC_RequestHomingParams = lib.ISC_RequestHomingParams
ISC_RequestHomingParams.restype = c_short
ISC_RequestHomingParams.argtypes = []


def request_homing_params(serial_number):
    '''
    Requests the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestHomingParams(serial_number)

    return output


ISC_RequestJogParams = lib.ISC_RequestJogParams
ISC_RequestJogParams.restype = c_short
ISC_RequestJogParams.argtypes = []


def request_jog_params(serial_number):
    '''
    Requests the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestJogParams(serial_number)

    return output


ISC_RequestLimitSwitchParams = lib.ISC_RequestLimitSwitchParams
ISC_RequestLimitSwitchParams.restype = c_short
ISC_RequestLimitSwitchParams.argtypes = []


def request_limit_switch_params(serial_number):
    '''
    Requests the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestLimitSwitchParams(serial_number)

    return output


ISC_RequestMoveAbsolutePosition = lib.ISC_RequestMoveAbsolutePosition
ISC_RequestMoveAbsolutePosition.restype = c_short
ISC_RequestMoveAbsolutePosition.argtypes = []


def request_move_absolute_position(serial_number):
    '''
    Requests the position of next absolute move.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestMoveAbsolutePosition(serial_number)

    return output


ISC_RequestMoveRelativeDistance = lib.ISC_RequestMoveRelativeDistance
ISC_RequestMoveRelativeDistance.restype = c_short
ISC_RequestMoveRelativeDistance.argtypes = []


def request_move_relative_distance(serial_number):
    '''
    Requests the relative move distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestMoveRelativeDistance(serial_number)

    return output


ISC_RequestPosition = lib.ISC_RequestPosition
ISC_RequestPosition.restype = c_short
ISC_RequestPosition.argtypes = []


def request_position(serial_number):
    '''
    Requests the current position.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestPosition(serial_number)

    return output


ISC_RequestPotentiometerParams = lib.ISC_RequestPotentiometerParams
ISC_RequestPotentiometerParams.restype = c_short
ISC_RequestPotentiometerParams.argtypes = []


def request_potentiometer_params(serial_number):
    '''
    Requests the potentiometer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestPotentiometerParams(serial_number)

    return output


ISC_RequestPowerParams = lib.ISC_RequestPowerParams
ISC_RequestPowerParams.restype = c_short
ISC_RequestPowerParams.argtypes = []


def request_power_params(serial_number):
    '''
    Requests the power parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestPowerParams(serial_number)

    return output


ISC_RequestSettings = lib.ISC_RequestSettings
ISC_RequestSettings.restype = c_short
ISC_RequestSettings.argtypes = []


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

    output = ISC_RequestSettings(serial_number)

    return output


ISC_RequestStatus = lib.ISC_RequestStatus
ISC_RequestStatus.restype = c_short
ISC_RequestStatus.argtypes = []


def request_status(serial_number):
    '''
    Request position and status bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestStatus(serial_number)

    return output


ISC_RequestStatusBits = lib.ISC_RequestStatusBits
ISC_RequestStatusBits.restype = c_short
ISC_RequestStatusBits.argtypes = []


def request_status_bits(serial_number):
    '''
    Request the status bits which identify the current motor state.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestStatusBits(serial_number)

    return output


ISC_RequestTriggerSwitches = lib.ISC_RequestTriggerSwitches
ISC_RequestTriggerSwitches.restype = c_short
ISC_RequestTriggerSwitches.argtypes = []


def request_trigger_switches(serial_number):
    '''
    Requests, gets or sets trigger switch bits for Cage Rotator only.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestTriggerSwitches(serial_number)

    return output


ISC_RequestVelParams = lib.ISC_RequestVelParams
ISC_RequestVelParams.restype = c_short
ISC_RequestVelParams.argtypes = []


def request_vel_params(serial_number):
    '''
    Requests the velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_RequestVelParams(serial_number)

    return output


ISC_ResetRotationModes = lib.ISC_ResetRotationModes
ISC_ResetRotationModes.restype = c_short
ISC_ResetRotationModes.argtypes = []


def reset_rotation_modes(serial_number):
    '''
    Reset the rotation modes for a rotational device.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_ResetRotationModes(serial_number)

    return output


ISC_ResetStageToDefaults = lib.ISC_ResetStageToDefaults
ISC_ResetStageToDefaults.restype = c_short
ISC_ResetStageToDefaults.argtypes = []


def reset_stage_to_defaults(serial_number):
    '''
    Reset the stage settings to defaults.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_ResetStageToDefaults(serial_number)

    return output


ISC_SetBacklash = lib.ISC_SetBacklash
ISC_SetBacklash.restype = c_short
ISC_SetBacklash.argtypes = []


def set_backlash(serial_number):
    '''
    Sets the backlash distance (used to control hysteresis).

    Parameters
    ----------
        serial_number: POINTER(c_char)
        distance: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    distance = c_long()

    output = ISC_SetBacklash(serial_number)

    return output


ISC_SetBowIndex = lib.ISC_SetBowIndex
ISC_SetBowIndex.restype = c_short
ISC_SetBowIndex.argtypes = []


def set_bow_index(serial_number):
    '''
    Sets the stepper motor bow index.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        bowIndex: c_short

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    bowIndex = c_short()

    output = ISC_SetBowIndex(serial_number)

    return output


ISC_SetButtonParams = lib.ISC_SetButtonParams
ISC_SetButtonParams.restype = c_short
ISC_SetButtonParams.argtypes = []


def set_button_params(serial_number):
    '''
    Sets the LTS button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonMode: MOT_ButtonModes
        leftButtonPosition: c_int
        rightButtonPosition: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonMode = MOT_ButtonModes()
    leftButtonPosition = c_int()
    rightButtonPosition = c_int()

    output = ISC_SetButtonParams(serial_number)

    return output


ISC_SetButtonParamsBlock = lib.ISC_SetButtonParamsBlock
ISC_SetButtonParamsBlock.restype = c_short
ISC_SetButtonParamsBlock.argtypes = []


def set_button_params_block(serial_number):
    '''
    Set the button parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        buttonParams: MOT_ButtonParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    buttonParams = MOT_ButtonParameters()

    output = ISC_SetButtonParamsBlock(serial_number)

    return output


ISC_SetCalibrationFile = lib.ISC_SetCalibrationFile
ISC_SetCalibrationFile.restype = c_void_p
ISC_SetCalibrationFile.argtypes = []


def set_calibration_file(serial_number):
    '''
    Set the calibration file for this motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        filename: POINTER(c_char)
        enabled: c_bool

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    filename = POINTER(c_char)()
    enabled = c_bool()

    output = ISC_SetCalibrationFile(serial_number)

    return output


ISC_SetDirection = lib.ISC_SetDirection
ISC_SetDirection.restype = c_void_p
ISC_SetDirection.argtypes = []


def set_direction(serial_number):
    '''
    Sets the motor direction sense.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        reverse: c_bool

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    reverse = c_bool()

    output = ISC_SetDirection(serial_number)

    return output


ISC_SetHomingParamsBlock = lib.ISC_SetHomingParamsBlock
ISC_SetHomingParamsBlock.restype = c_short
ISC_SetHomingParamsBlock.argtypes = []


def set_homing_params_block(serial_number):
    '''
    Set the homing parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        homingParams: MOT_HomingParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    homingParams = MOT_HomingParameters()

    output = ISC_SetHomingParamsBlock(serial_number)

    return output


ISC_SetHomingVelocity = lib.ISC_SetHomingVelocity
ISC_SetHomingVelocity.restype = c_short
ISC_SetHomingVelocity.argtypes = []


def set_homing_velocity(serial_number):
    '''
    Sets the homing velocity.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        velocity: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    velocity = c_uint()

    output = ISC_SetHomingVelocity(serial_number)

    return output


ISC_SetJogMode = lib.ISC_SetJogMode
ISC_SetJogMode.restype = c_short
ISC_SetJogMode.argtypes = []


def set_jog_mode(serial_number):
    '''
    Sets the jog mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: MOT_JogModes
        stopMode: MOT_StopModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = MOT_JogModes()
    stopMode = MOT_StopModes()

    output = ISC_SetJogMode(serial_number)

    return output


ISC_SetJogParamsBlock = lib.ISC_SetJogParamsBlock
ISC_SetJogParamsBlock.restype = c_short
ISC_SetJogParamsBlock.argtypes = []


def set_jog_params_block(serial_number):
    '''
    Set the jog parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        jogParams: MOT_JogParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    jogParams = MOT_JogParameters()

    output = ISC_SetJogParamsBlock(serial_number)

    return output


ISC_SetJogStepSize = lib.ISC_SetJogStepSize
ISC_SetJogStepSize.restype = c_short
ISC_SetJogStepSize.argtypes = []


def set_jog_step_size(serial_number):
    '''
    Sets the distance to move on jogging.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepSize: c_uint

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepSize = c_uint()

    output = ISC_SetJogStepSize(serial_number)

    return output


ISC_SetJogVelParams = lib.ISC_SetJogVelParams
ISC_SetJogVelParams.restype = c_short
ISC_SetJogVelParams.argtypes = []


def set_jog_vel_params(serial_number):
    '''
    Sets jog velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_SetJogVelParams(serial_number)

    return output


ISC_SetLEDswitches = lib.ISC_SetLEDswitches
ISC_SetLEDswitches.restype = c_short
ISC_SetLEDswitches.argtypes = []


def set_l_e_dswitches(serial_number):
    '''
    Set the LED indicator bits on device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        LEDswitches: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    LEDswitches = c_long()

    output = ISC_SetLEDswitches(serial_number)

    return output


ISC_SetLimitSwitchParams = lib.ISC_SetLimitSwitchParams
ISC_SetLimitSwitchParams.restype = c_short
ISC_SetLimitSwitchParams.argtypes = []


def set_limit_switch_params(serial_number):
    '''
    Sets the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        clockwiseHardwareLimit: MOT_LimitSwitchModes
        anticlockwiseHardwareLimit: MOT_LimitSwitchModes
        clockwisePosition: c_uint
        anticlockwisePosition: c_uint
        softLimitMode: MOT_LimitSwitchSWModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    clockwiseHardwareLimit = MOT_LimitSwitchModes()
    anticlockwiseHardwareLimit = MOT_LimitSwitchModes()
    clockwisePosition = c_uint()
    anticlockwisePosition = c_uint()
    softLimitMode = MOT_LimitSwitchSWModes()

    output = ISC_SetLimitSwitchParams(serial_number)

    return output


ISC_SetLimitSwitchParamsBlock = lib.ISC_SetLimitSwitchParamsBlock
ISC_SetLimitSwitchParamsBlock.restype = c_short
ISC_SetLimitSwitchParamsBlock.argtypes = []


def set_limit_switch_params_block(serial_number):
    '''
    Set the limit switch parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        limitSwitchParams: MOT_LimitSwitchParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    limitSwitchParams = MOT_LimitSwitchParameters()

    output = ISC_SetLimitSwitchParamsBlock(serial_number)

    return output


ISC_SetLimitsSoftwareApproachPolicy = lib.ISC_SetLimitsSoftwareApproachPolicy
ISC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
ISC_SetLimitsSoftwareApproachPolicy.argtypes = []


def set_limits_software_approach_policy(serial_number):
    '''
    Sets the software limits mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        limitsSoftwareApproachPolicy: MOT_LimitsSoftwareApproachPolicy

    Returns
    -------
        c_void_p
    '''

    serial_number = c_char_pointer(serial_number)
    limitsSoftwareApproachPolicy = MOT_LimitsSoftwareApproachPolicy()

    output = ISC_SetLimitsSoftwareApproachPolicy(serial_number)

    return output


ISC_SetMotorParams = lib.ISC_SetMotorParams
ISC_SetMotorParams.restype = c_short
ISC_SetMotorParams.argtypes = []


def set_motor_params(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_long
        gearBoxRatio: c_long
        pitch: c_float

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_long()
    gearBoxRatio = c_long()
    pitch = c_float()

    output = ISC_SetMotorParams(serial_number)

    return output


ISC_SetMotorParamsExt = lib.ISC_SetMotorParamsExt
ISC_SetMotorParamsExt.restype = c_short
ISC_SetMotorParamsExt.argtypes = []


def set_motor_params_ext(serial_number):
    '''
    Sets the motor stage parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        stepsPerRev: c_double
        gearBoxRatio: c_double
        pitch: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    stepsPerRev = c_double()
    gearBoxRatio = c_double()
    pitch = c_double()

    output = ISC_SetMotorParamsExt(serial_number)

    return output


ISC_SetMotorTravelLimits = lib.ISC_SetMotorTravelLimits
ISC_SetMotorTravelLimits.restype = c_short
ISC_SetMotorTravelLimits.argtypes = []


def set_motor_travel_limits(serial_number):
    '''
    Sets the absolute minimum and maximum travel range constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        minPosition: c_double
        maxPosition: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    minPosition = c_double()
    maxPosition = c_double()

    output = ISC_SetMotorTravelLimits(serial_number)

    return output


ISC_SetMotorTravelMode = lib.ISC_SetMotorTravelMode
ISC_SetMotorTravelMode.restype = c_short
ISC_SetMotorTravelMode.argtypes = []


def set_motor_travel_mode(serial_number):
    '''
    Set the motor travel mode.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        travelMode: MOT_TravelModes

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    travelMode = MOT_TravelModes()

    output = ISC_SetMotorTravelMode(serial_number)

    return output


ISC_SetMotorVelocityLimits = lib.ISC_SetMotorVelocityLimits
ISC_SetMotorVelocityLimits.restype = c_short
ISC_SetMotorVelocityLimits.argtypes = []


def set_motor_velocity_limits(serial_number):
    '''
    Sets the absolute maximum velocity and acceleration constants for the current stage.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        maxVelocity: c_double
        maxAcceleration: c_double

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    maxVelocity = c_double()
    maxAcceleration = c_double()

    output = ISC_SetMotorVelocityLimits(serial_number)

    return output


ISC_SetMoveAbsolutePosition = lib.ISC_SetMoveAbsolutePosition
ISC_SetMoveAbsolutePosition.restype = c_short
ISC_SetMoveAbsolutePosition.argtypes = []


def set_move_absolute_position(serial_number):
    '''
    Sets the move absolute position.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        position: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    position = c_int()

    output = ISC_SetMoveAbsolutePosition(serial_number)

    return output


ISC_SetMoveRelativeDistance = lib.ISC_SetMoveRelativeDistance
ISC_SetMoveRelativeDistance.restype = c_short
ISC_SetMoveRelativeDistance.argtypes = []


def set_move_relative_distance(serial_number):
    '''
    Sets the move relative distance.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        distance: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    distance = c_int()

    output = ISC_SetMoveRelativeDistance(serial_number)

    return output


ISC_SetPositionCounter = lib.ISC_SetPositionCounter
ISC_SetPositionCounter.restype = c_short
ISC_SetPositionCounter.argtypes = []


def set_position_counter(serial_number):
    '''
    Set the Position Counter.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        count: c_long

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    count = c_long()

    output = ISC_SetPositionCounter(serial_number)

    return output


ISC_SetPotentiometerParams = lib.ISC_SetPotentiometerParams
ISC_SetPotentiometerParams.restype = c_short
ISC_SetPotentiometerParams.argtypes = []


def set_potentiometer_params(serial_number):
    '''
    Sets the potentiometer parameters for the LTS.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        index: c_short
        thresholdDeflection: c_long
        velocity: c_ulong

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    index = c_short()
    thresholdDeflection = c_long()
    velocity = c_ulong()

    output = ISC_SetPotentiometerParams(serial_number)

    return output


ISC_SetPotentiometerParamsBlock = lib.ISC_SetPotentiometerParamsBlock
ISC_SetPotentiometerParamsBlock.restype = c_short
ISC_SetPotentiometerParamsBlock.argtypes = []


def set_potentiometer_params_block(serial_number):
    '''
    Set the potentiometer parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        potentiometerSteps: MOT_PotentiometerSteps

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    potentiometerSteps = MOT_PotentiometerSteps()

    output = ISC_SetPotentiometerParamsBlock(serial_number)

    return output


ISC_SetPowerParams = lib.ISC_SetPowerParams
ISC_SetPowerParams.restype = c_short
ISC_SetPowerParams.argtypes = []


def set_power_params(serial_number):
    '''
    Sets the power parameters for the stepper motor.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        powerParams: MOT_PowerParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    powerParams = MOT_PowerParameters()

    output = ISC_SetPowerParams(serial_number)

    return output


ISC_SetRotationModes = lib.ISC_SetRotationModes
ISC_SetRotationModes.restype = c_short
ISC_SetRotationModes.argtypes = []


def set_rotation_modes(serial_number):
    '''
    Set the rotation modes for a rotational device.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        mode: MOT_MovementModes
        direction: MOT_MovementDirections

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    mode = MOT_MovementModes()
    direction = MOT_MovementDirections()

    output = ISC_SetRotationModes(serial_number)

    return output


ISC_SetStageAxisLimits = lib.ISC_SetStageAxisLimits
ISC_SetStageAxisLimits.restype = c_short
ISC_SetStageAxisLimits.argtypes = []


def set_stage_axis_limits(serial_number):
    '''
    Sets the stage axis position limits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        minPosition: c_int
        maxPosition: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    minPosition = c_int()
    maxPosition = c_int()

    output = ISC_SetStageAxisLimits(serial_number)

    return output


ISC_SetTriggerSwitches = lib.ISC_SetTriggerSwitches
ISC_SetTriggerSwitches.restype = c_short
ISC_SetTriggerSwitches.argtypes = []


def set_trigger_switches(serial_number):
    '''
    Sets the trigger switch bits.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        indicatorBits: c_byte

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    indicatorBits = c_byte()

    output = ISC_SetTriggerSwitches(serial_number)

    return output


ISC_SetVelParams = lib.ISC_SetVelParams
ISC_SetVelParams.restype = c_short
ISC_SetVelParams.argtypes = []


def set_vel_params(serial_number):
    '''
    Sets the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        acceleration: c_int
        maxVelocity: c_int

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    acceleration = c_int()
    maxVelocity = c_int()

    output = ISC_SetVelParams(serial_number)

    return output


ISC_SetVelParamsBlock = lib.ISC_SetVelParamsBlock
ISC_SetVelParamsBlock.restype = c_short
ISC_SetVelParamsBlock.argtypes = []


def set_vel_params_block(serial_number):
    '''
    Set the move velocity parameters.

    Parameters
    ----------
        serial_number: POINTER(c_char)
        velocityParams: MOT_VelocityParameters

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)
    velocityParams = MOT_VelocityParameters()

    output = ISC_SetVelParamsBlock(serial_number)

    return output


ISC_StartPolling = lib.ISC_StartPolling
ISC_StartPolling.restype = c_bool
ISC_StartPolling.argtypes = []


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

    output = ISC_StartPolling(serial_number)

    return output


ISC_StopImmediate = lib.ISC_StopImmediate
ISC_StopImmediate.restype = c_short
ISC_StopImmediate.argtypes = []


def stop_immediate(serial_number):
    '''
    Stop the current move immediately (with risk of losing track of position).

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_StopImmediate(serial_number)

    return output


ISC_StopPolling = lib.ISC_StopPolling
ISC_StopPolling.restype = c_void_p
ISC_StopPolling.argtypes = []


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

    output = ISC_StopPolling(serial_number)

    return output


ISC_StopProfiled = lib.ISC_StopProfiled
ISC_StopProfiled.restype = c_short
ISC_StopProfiled.argtypes = []


def stop_profiled(serial_number):
    '''
    Stop the current move using the current velocity profile.

    Parameters
    ----------
        serial_number: POINTER(c_char)

    Returns
    -------
        c_short
    '''

    serial_number = c_char_pointer(serial_number)

    output = ISC_StopProfiled(serial_number)

    return output


ISC_TimeSinceLastMsgReceived = lib.ISC_TimeSinceLastMsgReceived
ISC_TimeSinceLastMsgReceived.restype = c_bool
ISC_TimeSinceLastMsgReceived.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    lastUpdateTimeMS = c_int64()

    output = ISC_TimeSinceLastMsgReceived(serial_number)

    return output


ISC_WaitForMessage = lib.ISC_WaitForMessage
ISC_WaitForMessage.restype = c_bool
ISC_WaitForMessage.argtypes = []


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

    serial_number = c_char_pointer(serial_number)
    messageType = c_long()
    messageID = c_long()
    messageData = c_ulong()

    output = ISC_WaitForMessage(serial_number)

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



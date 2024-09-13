from ctypes import (
    POINTER,
    c_bool,
    c_byte,
    c_char,
    c_double,
    c_int,
    c_int16,
    c_int32,
    c_int64,
    c_long,
    c_short,
    c_uint,
    c_ulong,
    c_void_p,
    cdll)
from .definitions.safearray import SafeArray
from .definitions.enumerations import (
    MOD_AuxIOPortMode,
    MOD_IOPortMode,
    MOD_IOPortSource,
    MOD_Monitor_Variable,
    MOT_JogModes,
    MOT_LimitsSoftwareApproachPolicy,
    MOT_MovementDirections,
    MOT_MovementModes,
    MOT_RasterScanMoveCmd,
    MOT_StopModes,
    MOT_TravelDirection,
    MOT_TravelModes,
    MOT_TriggerInputConfigModes,
    MOT_TriggerInputSource,
    MOT_TriggerOutputConfigModes,
    MOT_TriggerPolarity,
    MOT_TriggerState)
from .definitions.structures import (
    MOD_AnalogMonitorConfigurationParameters,
    MOD_AuxIOPortConfigurationParameters,
    MOD_AuxIOPortConfigurationSetParameters,
    MOD_IOPortConfigurationParameters,
    MOT_BrushlessCurrentLoopParameters,
    MOT_BrushlessElectricOutputParameters,
    MOT_BrushlessPositionLoopParameters,
    MOT_BrushlessTrackSettleParameters,
    MOT_ChannelPosition,
    MOT_HomingParameters,
    MOT_JogParameters,
    MOT_JoystickParameters,
    MOT_LCDMoveParams,
    MOT_LCDParams,
    MOT_RasterScanMoveParams,
    MOT_StageAxisParameters,
    MOT_TriggerIOConfigParameters,
    MOT_VelocityParameters,
    MOT_VelocityProfileParameters,
    TLI_DeviceInfo)


lib_path = "C:/Program Files/Thorlabs/Kinesis/"
device_manager = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.DeviceManager.dll")

lib = cdll.LoadLibrary(
    lib_path + "Thorlabs.MotionControl.Benchtop.BrushlessMotor.dll")


# Build the DeviceList.
TLI_BuildDeviceList = lib.TLI_BuildDeviceList
TLI_BuildDeviceList.restype = c_short
TLI_BuildDeviceList.argtypes = []


# Initialize a connection to the Simulation Manager, which must already be running.
TLI_InitializeSimulations = lib.TLI_InitializeSimulations
TLI_InitializeSimulations.restype = c_void_p
TLI_InitializeSimulations.argtypes = []


# Can the device perform a Home.
BMC_CanHome = lib.BMC_CanHome
BMC_CanHome.restype = c_bool
BMC_CanHome.argtypes = [POINTER(c_char), c_short]


# Can this device be moved without Homing.
BMC_CanMoveWithoutHomingFirst = lib.BMC_CanMoveWithoutHomingFirst
BMC_CanMoveWithoutHomingFirst.restype = c_bool
BMC_CanMoveWithoutHomingFirst.argtypes = [POINTER(c_char), c_short]


# Check connection.
BMC_CheckConnection = lib.BMC_CheckConnection
BMC_CheckConnection.restype = c_bool
BMC_CheckConnection.argtypes = [POINTER(c_char)]


# Clears the device message queue.
BMC_ClearMessageQueue = lib.BMC_ClearMessageQueue
BMC_ClearMessageQueue.restype = c_short
BMC_ClearMessageQueue.argtypes = [POINTER(c_char), c_short]


# Disconnect and close the device.
BMC_Close = lib.BMC_Close
BMC_Close.restype = c_short
BMC_Close.argtypes = [POINTER(c_char)]


# Disable the channel so that motor can be moved by hand.
BMC_DisableChannel = lib.BMC_DisableChannel
BMC_DisableChannel.restype = c_short
BMC_DisableChannel.argtypes = [POINTER(c_char), c_short]


# Enable channel for computer control.
BMC_EnableChannel = lib.BMC_EnableChannel
BMC_EnableChannel.restype = c_short
BMC_EnableChannel.argtypes = [POINTER(c_char), c_short]


# Enables the last message monitoring timer.
BMC_EnableLastMsgTimer = lib.BMC_EnableLastMsgTimer
BMC_EnableLastMsgTimer.restype = c_void_p
BMC_EnableLastMsgTimer.argtypes = [POINTER(c_char), c_short, c_bool, c_int32]


# Gets the Analog Monitor Config Parameters.
BMC_GetAnalogMonitorConfigParams = lib.BMC_GetAnalogMonitorConfigParams
BMC_GetAnalogMonitorConfigParams.restype = c_short
BMC_GetAnalogMonitorConfigParams.argtypes = [POINTER(c_char), c_byte, c_long, MOD_Monitor_Variable, c_long, c_long]


# Gets the Analog Monitor Config Parameters.
BMC_GetAnalogMonitorConfigParamsBlock = lib.BMC_GetAnalogMonitorConfigParamsBlock
BMC_GetAnalogMonitorConfigParamsBlock.restype = c_short
BMC_GetAnalogMonitorConfigParamsBlock.argtypes = [POINTER(c_char), c_byte, MOD_AnalogMonitorConfigurationParameters]


# Gets the Aux IO Port Config Parameters.
BMC_GetAuxIOPortConfigParams = lib.BMC_GetAuxIOPortConfigParams
BMC_GetAuxIOPortConfigParams.restype = c_short
BMC_GetAuxIOPortConfigParams.argtypes = [POINTER(c_char), c_byte, MOD_AuxIOPortMode, c_long]


# Gets the Aux IO Port Config Parameters.
BMC_GetAuxIOPortConfigParamsBlock = lib.BMC_GetAuxIOPortConfigParamsBlock
BMC_GetAuxIOPortConfigParamsBlock.restype = c_short
BMC_GetAuxIOPortConfigParamsBlock.argtypes = [POINTER(c_char), c_byte, MOD_AuxIOPortConfigurationParameters]


# Get the backlash distance setting (used to control hysteresis).
BMC_GetBacklash = lib.BMC_GetBacklash
BMC_GetBacklash.restype = c_long
BMC_GetBacklash.argtypes = [POINTER(c_char), c_short]


# Gets the current loop parameters for moving to required position.
BMC_GetCurrentLoopParams = lib.BMC_GetCurrentLoopParams
BMC_GetCurrentLoopParams.restype = c_short
BMC_GetCurrentLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessCurrentLoopParameters]


# Converts a device unit to a real world unit.
BMC_GetDeviceUnitFromRealValue = lib.BMC_GetDeviceUnitFromRealValue
BMC_GetDeviceUnitFromRealValue.restype = c_short
BMC_GetDeviceUnitFromRealValue.argtypes = [POINTER(c_char), c_short, c_double, c_int, c_int]


# Gets the digital output bits.
BMC_GetDigitalOutputs = lib.BMC_GetDigitalOutputs
BMC_GetDigitalOutputs.restype = c_byte
BMC_GetDigitalOutputs.argtypes = [POINTER(c_char), c_short]


# Gets the electric output parameters.
BMC_GetElectricOutputParams = lib.BMC_GetElectricOutputParams
BMC_GetElectricOutputParams.restype = c_short
BMC_GetElectricOutputParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessElectricOutputParameters]


# Get the Encoder Counter.
BMC_GetEncoderCounter = lib.BMC_GetEncoderCounter
BMC_GetEncoderCounter.restype = c_long
BMC_GetEncoderCounter.argtypes = [POINTER(c_char), c_short]


# Gets version number of the device firmware.
BMC_GetFirmwareVersion = lib.BMC_GetFirmwareVersion
BMC_GetFirmwareVersion.restype = c_ulong
BMC_GetFirmwareVersion.argtypes = [POINTER(c_char), c_short]


# Gets the hardware information from the device.
BMC_GetHardwareInfo = lib.BMC_GetHardwareInfo
BMC_GetHardwareInfo.restype = c_short
BMC_GetHardwareInfo.argtypes = [POINTER(c_char)]


# Gets the hardware information in a block.
BMC_GetHardwareInfoBlock = lib.BMC_GetHardwareInfoBlock
BMC_GetHardwareInfoBlock.restype = c_short
BMC_GetHardwareInfoBlock.argtypes = [POINTER(c_char)]


# Get the homing parameters.
BMC_GetHomingParamsBlock = lib.BMC_GetHomingParamsBlock
BMC_GetHomingParamsBlock.restype = c_short
BMC_GetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


# Gets the homing velocity.
BMC_GetHomingVelocity = lib.BMC_GetHomingVelocity
BMC_GetHomingVelocity.restype = c_uint
BMC_GetHomingVelocity.argtypes = [POINTER(c_char), c_short]


# Gets the IO Port Config Parameters.
BMC_GetIOPortConfigParams = lib.BMC_GetIOPortConfigParams
BMC_GetIOPortConfigParams.restype = c_short
BMC_GetIOPortConfigParams.argtypes = [POINTER(c_char), c_byte, MOD_IOPortMode, MOD_IOPortSource]


# Gets the IO Port Config Parameters.
BMC_GetIOPortConfigParamsBlock = lib.BMC_GetIOPortConfigParamsBlock
BMC_GetIOPortConfigParamsBlock.restype = c_short
BMC_GetIOPortConfigParamsBlock.argtypes = [POINTER(c_char), c_byte, MOD_IOPortConfigurationParameters]


# Gets the jog mode.
BMC_GetJogMode = lib.BMC_GetJogMode
BMC_GetJogMode.restype = c_short
BMC_GetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


# Get the jog parameters.
BMC_GetJogParamsBlock = lib.BMC_GetJogParamsBlock
BMC_GetJogParamsBlock.restype = c_short
BMC_GetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters]


# Gets the distance to move when jogging.
BMC_GetJogStepSize = lib.BMC_GetJogStepSize
BMC_GetJogStepSize.restype = c_uint
BMC_GetJogStepSize.argtypes = [POINTER(c_char), c_short]


# Gets the jog velocity parameters.
BMC_GetJogVelParams = lib.BMC_GetJogVelParams
BMC_GetJogVelParams.restype = c_short
BMC_GetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


# Gets the joystick parameters.
BMC_GetJoystickParams = lib.BMC_GetJoystickParams
BMC_GetJoystickParams.restype = c_short
BMC_GetJoystickParams.argtypes = [POINTER(c_char), c_short, MOT_JoystickParameters]


# Get the Parameters for Motion from the LCD Display Interface.
BMC_GetLCDMoveParams = lib.BMC_GetLCDMoveParams
BMC_GetLCDMoveParams.restype = c_short
BMC_GetLCDMoveParams.argtypes = [
    POINTER(c_char), c_short, MOT_JogModes, c_int32,
    c_int32, c_int32, MOT_StopModes, c_int32, c_int32, c_int32]


# Gets the LCD parameters for the device.
BMC_GetLCDMoveParamsBlock = lib.BMC_GetLCDMoveParamsBlock
BMC_GetLCDMoveParamsBlock.restype = c_short
BMC_GetLCDMoveParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LCDMoveParams]


# Get the LCD Parameters for the Benchtop Display Interface.
BMC_GetLCDParams = lib.BMC_GetLCDParams
BMC_GetLCDParams.restype = c_short
BMC_GetLCDParams.argtypes = [POINTER(c_char), c_int16, c_int16, c_int16, c_int16]


# Gets the LCD parameters for the device.
BMC_GetLCDParamsBlock = lib.BMC_GetLCDParamsBlock
BMC_GetLCDParamsBlock.restype = c_short
BMC_GetLCDParamsBlock.argtypes = [POINTER(c_char), MOT_LCDParams]


# Get the motor parameters for the Brushless Votor.
BMC_GetMotorParams = lib.BMC_GetMotorParams
BMC_GetMotorParams.restype = c_short
BMC_GetMotorParams.argtypes = [POINTER(c_char), c_short, c_long]


# Get the motor parameters for the Brushless Votor.
BMC_GetMotorParamsExt = lib.BMC_GetMotorParamsExt
BMC_GetMotorParamsExt.restype = c_short
BMC_GetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double]


# Gets the absolute minimum and maximum travel range constants for the current stage.
BMC_GetMotorTravelLimits = lib.BMC_GetMotorTravelLimits
BMC_GetMotorTravelLimits.restype = c_short
BMC_GetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


# Get motor travel mode.
BMC_GetMotorTravelMode = lib.BMC_GetMotorTravelMode
BMC_GetMotorTravelMode.restype = MOT_TravelModes
BMC_GetMotorTravelMode.argtypes = [POINTER(c_char), c_short]


# Gets the absolute maximum velocity and acceleration constants for the current stage.
BMC_GetMotorVelocityLimits = lib.BMC_GetMotorVelocityLimits
BMC_GetMotorVelocityLimits.restype = c_short
BMC_GetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


# Gets the move absolute position.
BMC_GetMoveAbsolutePosition = lib.BMC_GetMoveAbsolutePosition
BMC_GetMoveAbsolutePosition.restype = c_int
BMC_GetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]


# Gets the move relative distance.
BMC_GetMoveRelativeDistance = lib.BMC_GetMoveRelativeDistance
BMC_GetMoveRelativeDistance.restype = c_int
BMC_GetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


# Get the next MessageQueue item.
BMC_GetNextMessage = lib.BMC_GetNextMessage
BMC_GetNextMessage.restype = c_bool
BMC_GetNextMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


# Gets the number of channels in the device.
BMC_GetNumChannels = lib.BMC_GetNumChannels
BMC_GetNumChannels.restype = c_short
BMC_GetNumChannels.argtypes = [POINTER(c_char)]


# Get number of positions.
BMC_GetNumberPositions = lib.BMC_GetNumberPositions
BMC_GetNumberPositions.restype = c_int
BMC_GetNumberPositions.argtypes = [POINTER(c_char), c_short]


# Gets the position feedback loop parameters.
BMC_GetPosLoopParams = lib.BMC_GetPosLoopParams
BMC_GetPosLoopParams.restype = c_short
BMC_GetPosLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessPositionLoopParameters]


# Get the current position.
BMC_GetPosition = lib.BMC_GetPosition
BMC_GetPosition.restype = c_int
BMC_GetPosition.argtypes = [POINTER(c_char), c_short]


# Get the Position Counter.
BMC_GetPositionCounter = lib.BMC_GetPositionCounter
BMC_GetPositionCounter.restype = c_long
BMC_GetPositionCounter.argtypes = [POINTER(c_char), c_short]


# Gets the Position Trigger state.
BMC_GetPositionTriggerState = lib.BMC_GetPositionTriggerState
BMC_GetPositionTriggerState.restype = c_short
BMC_GetPositionTriggerState.argtypes = [POINTER(c_char), c_short, MOT_TriggerState]


# Gets the rack digital output bits.
BMC_GetRackDigitalOutputs = lib.BMC_GetRackDigitalOutputs
BMC_GetRackDigitalOutputs.restype = c_byte
BMC_GetRackDigitalOutputs.argtypes = [POINTER(c_char)]


# Gets the Rack status bits.
BMC_GetRackStatusBits = lib.BMC_GetRackStatusBits
BMC_GetRackStatusBits.restype = c_ulong
BMC_GetRackStatusBits.argtypes = [POINTER(c_char)]


# Get the Raster Scan Move Parameters .
BMC_GetRasterScanMoveParams = lib.BMC_GetRasterScanMoveParams
BMC_GetRasterScanMoveParams.restype = c_short
BMC_GetRasterScanMoveParams.argtypes = [POINTER(c_char), MOT_RasterScanMoveParams]


# Converts a device unit to a real world unit.
BMC_GetRealValueFromDeviceUnit = lib.BMC_GetRealValueFromDeviceUnit
BMC_GetRealValueFromDeviceUnit.restype = c_short
BMC_GetRealValueFromDeviceUnit.argtypes = [POINTER(c_char), c_short, c_int, c_double, c_int]


# Gets the settled current loop parameters for holding at required position.
BMC_GetSettledCurrentLoopParams = lib.BMC_GetSettledCurrentLoopParams
BMC_GetSettledCurrentLoopParams.restype = c_short
BMC_GetSettledCurrentLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessCurrentLoopParameters]


# Gets the software limits mode.
BMC_GetSoftLimitMode = lib.BMC_GetSoftLimitMode
BMC_GetSoftLimitMode.restype = MOT_LimitsSoftwareApproachPolicy
BMC_GetSoftLimitMode.argtypes = [POINTER(c_char), c_short]


# Gets version number of the device software.
BMC_GetSoftwareVersion = lib.BMC_GetSoftwareVersion
BMC_GetSoftwareVersion.restype = c_ulong
BMC_GetSoftwareVersion.argtypes = [POINTER(c_char)]


# Gets the Brushless Motor stage axis maximum position.
BMC_GetStageAxisMaxPos = lib.BMC_GetStageAxisMaxPos
BMC_GetStageAxisMaxPos.restype = c_int
BMC_GetStageAxisMaxPos.argtypes = [POINTER(c_char), c_short]


# Gets the Brushless Motor stage axis minimum position.
BMC_GetStageAxisMinPos = lib.BMC_GetStageAxisMinPos
BMC_GetStageAxisMinPos.restype = c_int
BMC_GetStageAxisMinPos.argtypes = [POINTER(c_char), c_short]


# Gets the Brushless Motor stage axis parameters.
BMC_GetStageAxisParams = lib.BMC_GetStageAxisParams
BMC_GetStageAxisParams.restype = c_short
BMC_GetStageAxisParams.argtypes = [
    POINTER(c_char), c_short, c_long, c_long, POINTER(c_char),
    c_ulong, c_ulong, c_ulong, c_int, c_int, c_int, c_int, c_int]


# Gets the Brushless Motor stage axis parameters.
BMC_GetStageAxisParamsBlock = lib.BMC_GetStageAxisParamsBlock
BMC_GetStageAxisParamsBlock.restype = c_short
BMC_GetStageAxisParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_StageAxisParameters]


# Get the current status bits.
BMC_GetStatusBits = lib.BMC_GetStatusBits
BMC_GetStatusBits.restype = c_ulong
BMC_GetStatusBits.argtypes = [POINTER(c_char), c_short]


# Gets the track settled parameters used to decide when settled at right position.
BMC_GetTrackSettleParams = lib.BMC_GetTrackSettleParams
BMC_GetTrackSettleParams.restype = c_short
BMC_GetTrackSettleParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessTrackSettleParameters]


# Gets the IO Trigger Config Parameters.
BMC_GetTriggerIOConfigParams = lib.BMC_GetTriggerIOConfigParams
BMC_GetTriggerIOConfigParams.restype = c_short
BMC_GetTriggerIOConfigParams.argtypes = [
    POINTER(c_char),
    c_short,
    MOT_TriggerInputConfigModes,
    MOT_TriggerPolarity,
    MOT_TriggerInputSource,
    MOT_TriggerOutputConfigModes,
    MOT_TriggerPolarity,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long]


# Gets the IO Trigger Config Parameters.
BMC_GetTriggerIOConfigParamsBlock = lib.BMC_GetTriggerIOConfigParamsBlock
BMC_GetTriggerIOConfigParamsBlock.restype = c_short
BMC_GetTriggerIOConfigParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_TriggerIOConfigParameters]


# Gets the trigger switch bits.
BMC_GetTriggerSwitches = lib.BMC_GetTriggerSwitches
BMC_GetTriggerSwitches.restype = c_byte
BMC_GetTriggerSwitches.argtypes = [POINTER(c_char), c_short]


# Gets the move velocity parameters.
BMC_GetVelParams = lib.BMC_GetVelParams
BMC_GetVelParams.restype = c_short
BMC_GetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


# Get the move velocity parameters.
BMC_GetVelParamsBlock = lib.BMC_GetVelParamsBlock
BMC_GetVelParamsBlock.restype = c_short
BMC_GetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters]


# Gets the velocity profile parameters.
BMC_GetVelocityProfileParams = lib.BMC_GetVelocityProfileParams
BMC_GetVelocityProfileParams.restype = c_short
BMC_GetVelocityProfileParams.argtypes = [POINTER(c_char), c_short, MOT_VelocityProfileParameters]


# Queries if the time since the last message has exceeded the
# lastMsgTimeout set by BMC_EnableLastMsgTimer(char const * serialNo, bool
# enable, __int32 lastMsgTimeout ).
BMC_HasLastMsgTimerOverrun = lib.BMC_HasLastMsgTimerOverrun
BMC_HasLastMsgTimerOverrun.restype = c_bool
BMC_HasLastMsgTimerOverrun.argtypes = [POINTER(c_char), c_short]


# Home the device.
BMC_Home = lib.BMC_Home
BMC_Home.restype = c_short
BMC_Home.argtypes = [POINTER(c_char), c_short]


# Sends a command to the device to make it identify iteself.
BMC_Identify = lib.BMC_Identify
BMC_Identify.restype = c_void_p
BMC_Identify.argtypes = [POINTER(c_char)]


# Verifies that the specified channel is valid.
BMC_IsChannelValid = lib.BMC_IsChannelValid
BMC_IsChannelValid.restype = c_bool
BMC_IsChannelValid.argtypes = [POINTER(c_char), c_short]


# Update device with named settings.
BMC_LoadNamedSettings = lib.BMC_LoadNamedSettings
BMC_LoadNamedSettings.restype = c_bool
BMC_LoadNamedSettings.argtypes = [POINTER(c_char), c_short, POINTER(c_char)]


# Update device with stored settings.
BMC_LoadSettings = lib.BMC_LoadSettings
BMC_LoadSettings.restype = c_bool
BMC_LoadSettings.argtypes = [POINTER(c_char), c_short]


# Gets the number of channels available to this device.
BMC_MaxChannelCount = lib.BMC_MaxChannelCount
BMC_MaxChannelCount.restype = c_int
BMC_MaxChannelCount.argtypes = [POINTER(c_char)]


# Gets the MessageQueue size.
BMC_MessageQueueSize = lib.BMC_MessageQueueSize
BMC_MessageQueueSize.restype = c_int
BMC_MessageQueueSize.argtypes = [POINTER(c_char), c_short]


# Moves the device to the position defined in the SetMoveAbsolute command.
BMC_MoveAbsolute = lib.BMC_MoveAbsolute
BMC_MoveAbsolute.restype = c_short
BMC_MoveAbsolute.argtypes = [POINTER(c_char), c_short]


# Start moving at the current velocity in the specified direction.
BMC_MoveAtVelocity = lib.BMC_MoveAtVelocity
BMC_MoveAtVelocity.restype = c_short
BMC_MoveAtVelocity.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


# Perform a jog.
BMC_MoveJog = lib.BMC_MoveJog
BMC_MoveJog.restype = c_short
BMC_MoveJog.argtypes = [POINTER(c_char), c_short, MOT_TravelDirection]


# Move the motor by a relative amount.
BMC_MoveRelative = lib.BMC_MoveRelative
BMC_MoveRelative.restype = c_short
BMC_MoveRelative.argtypes = [POINTER(c_char), c_short, c_int]


# Moves the device by a relative distancce defined by SetMoveRelativeDistance.
BMC_MoveRelativeDistance = lib.BMC_MoveRelativeDistance
BMC_MoveRelativeDistance.restype = c_short
BMC_MoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


# Move the device to the specified position (index).
BMC_MoveToPosition = lib.BMC_MoveToPosition
BMC_MoveToPosition.restype = c_short
BMC_MoveToPosition.argtypes = [POINTER(c_char), c_short, c_int]


# Does the device need to be Homed before a move can be performed.
BMC_NeedsHoming = lib.BMC_NeedsHoming
BMC_NeedsHoming.restype = c_bool
BMC_NeedsHoming.argtypes = [POINTER(c_char), c_short]


# Open the device for communications.
BMC_Open = lib.BMC_Open
BMC_Open.restype = c_short
BMC_Open.argtypes = [POINTER(c_char)]


# Set to allow a device to be positioned without prior homing.
BMC_OverrideHomeRequirement = lib.BMC_OverrideHomeRequirement
BMC_OverrideHomeRequirement.restype = c_short
BMC_OverrideHomeRequirement.argtypes = [POINTER(c_char), c_short]


# persist the devices current settings.
BMC_PersistSettings = lib.BMC_PersistSettings
BMC_PersistSettings.restype = c_bool
BMC_PersistSettings.argtypes = [POINTER(c_char), c_short]


# Gets the polling loop duration.
BMC_PollingDuration = lib.BMC_PollingDuration
BMC_PollingDuration.restype = c_long
BMC_PollingDuration.argtypes = [POINTER(c_char), c_short]


# Starts a Raster Scan Move.
BMC_RasterScanMove = lib.BMC_RasterScanMove
BMC_RasterScanMove.restype = c_short
BMC_RasterScanMove.argtypes = [POINTER(c_char), MOT_RasterScanMoveCmd]


# Registers a callback on the message queue.
BMC_RegisterMessageCallback = lib.BMC_RegisterMessageCallback
BMC_RegisterMessageCallback.restype = c_short
BMC_RegisterMessageCallback.argtypes = [POINTER(c_char), c_short, c_void_p]


# Registers a callback in the event of synchronized move ending.
BMC_RegisterSynchronizedMoveCompleteCallback = lib.BMC_RegisterSynchronizedMoveCompleteCallback
BMC_RegisterSynchronizedMoveCompleteCallback.restype = c_short
BMC_RegisterSynchronizedMoveCompleteCallback.argtypes = [POINTER(c_char), c_void_p]


# Requests the Parameters for Analog Monitor config.
BMC_RequestAnalogMonitorConfigParams = lib.BMC_RequestAnalogMonitorConfigParams
BMC_RequestAnalogMonitorConfigParams.restype = c_short
BMC_RequestAnalogMonitorConfigParams.argtypes = [POINTER(c_char), c_byte]


# Requests the Parameters for Aux IO Port config.
BMC_RequestAuxIOPortConfigParams = lib.BMC_RequestAuxIOPortConfigParams
BMC_RequestAuxIOPortConfigParams.restype = c_short
BMC_RequestAuxIOPortConfigParams.argtypes = [POINTER(c_char), c_byte]


# Requests the backlash.
BMC_RequestBacklash = lib.BMC_RequestBacklash
BMC_RequestBacklash.restype = c_short
BMC_RequestBacklash.argtypes = [POINTER(c_char), c_short]


# Requests the current loop parameters for moving to required position.
BMC_RequestCurrentLoopParams = lib.BMC_RequestCurrentLoopParams
BMC_RequestCurrentLoopParams.restype = c_short
BMC_RequestCurrentLoopParams.argtypes = [POINTER(c_char), c_short]


# Requests the digital output bits.
BMC_RequestDigitalOutputs = lib.BMC_RequestDigitalOutputs
BMC_RequestDigitalOutputs.restype = c_short
BMC_RequestDigitalOutputs.argtypes = [POINTER(c_char), c_short]


# Requests the electric output parameters.
BMC_RequestElectricOutputParams = lib.BMC_RequestElectricOutputParams
BMC_RequestElectricOutputParams.restype = c_short
BMC_RequestElectricOutputParams.argtypes = [POINTER(c_char), c_short]


# Requests the encoder counter.
BMC_RequestEncoderCounter = lib.BMC_RequestEncoderCounter
BMC_RequestEncoderCounter.restype = c_short
BMC_RequestEncoderCounter.argtypes = [POINTER(c_char), c_short]


# Requests the homing parameters.
BMC_RequestHomingParams = lib.BMC_RequestHomingParams
BMC_RequestHomingParams.restype = c_short
BMC_RequestHomingParams.argtypes = [POINTER(c_char), c_short]


# Requests the Parameters for IO Port config.
BMC_RequestIOPortConfigParams = lib.BMC_RequestIOPortConfigParams
BMC_RequestIOPortConfigParams.restype = c_short
BMC_RequestIOPortConfigParams.argtypes = [POINTER(c_char), c_byte]


# Requests the jog parameters.
BMC_RequestJogParams = lib.BMC_RequestJogParams
BMC_RequestJogParams.restype = c_short
BMC_RequestJogParams.argtypes = [POINTER(c_char), c_short]


# Requests the joystick parameters.
BMC_RequestJoystickParams = lib.BMC_RequestJoystickParams
BMC_RequestJoystickParams.restype = c_short
BMC_RequestJoystickParams.argtypes = [POINTER(c_char), c_short]


# Requests the Parameters for Motion from the LCD Display Interface.
BMC_RequestLCDMoveParams = lib.BMC_RequestLCDMoveParams
BMC_RequestLCDMoveParams.restype = c_short
BMC_RequestLCDMoveParams.argtypes = [POINTER(c_char), c_short]


# Requests the LCD Parameters for the Benchtop Display Interface.
BMC_RequestLCDParams = lib.BMC_RequestLCDParams
BMC_RequestLCDParams.restype = c_short
BMC_RequestLCDParams.argtypes = [POINTER(c_char)]


# Requests the position of next absolute move.
BMC_RequestMoveAbsolutePosition = lib.BMC_RequestMoveAbsolutePosition
BMC_RequestMoveAbsolutePosition.restype = c_short
BMC_RequestMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short]


# Requests the relative move distance.
BMC_RequestMoveRelativeDistance = lib.BMC_RequestMoveRelativeDistance
BMC_RequestMoveRelativeDistance.restype = c_short
BMC_RequestMoveRelativeDistance.argtypes = [POINTER(c_char), c_short]


# Requests the position feedback loop parameters.
BMC_RequestPosLoopParams = lib.BMC_RequestPosLoopParams
BMC_RequestPosLoopParams.restype = c_short
BMC_RequestPosLoopParams.argtypes = [POINTER(c_char), c_short]


# Requests the current position.
BMC_RequestPosition = lib.BMC_RequestPosition
BMC_RequestPosition.restype = c_short
BMC_RequestPosition.argtypes = [POINTER(c_char), c_short]


# Requests the Parameters for Position Trigger state.
BMC_RequestPositionTriggerState = lib.BMC_RequestPositionTriggerState
BMC_RequestPositionTriggerState.restype = c_short
BMC_RequestPositionTriggerState.argtypes = [POINTER(c_char), c_short]


# Requests the rack digital output bits.
BMC_RequestRackDigitalOutputs = lib.BMC_RequestRackDigitalOutputs
BMC_RequestRackDigitalOutputs.restype = c_short
BMC_RequestRackDigitalOutputs.argtypes = [POINTER(c_char)]


# Requests the Rack status bits be downloaded.
BMC_RequestRackStatusBits = lib.BMC_RequestRackStatusBits
BMC_RequestRackStatusBits.restype = c_short
BMC_RequestRackStatusBits.argtypes = [POINTER(c_char)]


# requests the Raster Scan Move Parameters.
BMC_RequestRasterScanMoveParams = lib.BMC_RequestRasterScanMoveParams
BMC_RequestRasterScanMoveParams.restype = c_short
BMC_RequestRasterScanMoveParams.argtypes = [POINTER(c_char)]


# Requests that all settings are download from device.
BMC_RequestSettings = lib.BMC_RequestSettings
BMC_RequestSettings.restype = c_short
BMC_RequestSettings.argtypes = [POINTER(c_char), c_short]


# Requests the current loop parameters for holding at required position.
BMC_RequestSettledCurrentLoopParams = lib.BMC_RequestSettledCurrentLoopParams
BMC_RequestSettledCurrentLoopParams.restype = c_short
BMC_RequestSettledCurrentLoopParams.argtypes = [POINTER(c_char), c_short]


# Requests the stage axis parameters.
BMC_RequestStageAxisParams = lib.BMC_RequestStageAxisParams
BMC_RequestStageAxisParams.restype = c_short
BMC_RequestStageAxisParams.argtypes = [POINTER(c_char), c_short]


# Request the status bits which identify the current motor state.
BMC_RequestStatusBits = lib.BMC_RequestStatusBits
BMC_RequestStatusBits.restype = c_short
BMC_RequestStatusBits.argtypes = [POINTER(c_char), c_short]


# Requests the parameters used to decide when settled at right position.
BMC_RequestTrackSettleParams = lib.BMC_RequestTrackSettleParams
BMC_RequestTrackSettleParams.restype = c_short
BMC_RequestTrackSettleParams.argtypes = [POINTER(c_char), c_short]


# Requests the Parameters for IO config Trigger.
BMC_RequestTriggerIOConfigParams = lib.BMC_RequestTriggerIOConfigParams
BMC_RequestTriggerIOConfigParams.restype = c_short
BMC_RequestTriggerIOConfigParams.argtypes = [POINTER(c_char), c_short]


# Requests the trigger switch bits.
BMC_RequestTriggerSwitches = lib.BMC_RequestTriggerSwitches
BMC_RequestTriggerSwitches.restype = c_short
BMC_RequestTriggerSwitches.argtypes = [POINTER(c_char), c_short]


# Requests the velocity parameters.
BMC_RequestVelParams = lib.BMC_RequestVelParams
BMC_RequestVelParams.restype = c_short
BMC_RequestVelParams.argtypes = [POINTER(c_char), c_short]


# Requests the velocity profile parameters.
BMC_RequestVelocityProfileParams = lib.BMC_RequestVelocityProfileParams
BMC_RequestVelocityProfileParams.restype = c_short
BMC_RequestVelocityProfileParams.argtypes = [POINTER(c_char), c_short]


# Reset the rotation modes for a rotational device.
BMC_ResetRotationModes = lib.BMC_ResetRotationModes
BMC_ResetRotationModes.restype = c_short
BMC_ResetRotationModes.argtypes = [POINTER(c_char), c_short]


# Reset the stage settings to defaults.
BMC_ResetStageToDefaults = lib.BMC_ResetStageToDefaults
BMC_ResetStageToDefaults.restype = c_short
BMC_ResetStageToDefaults.argtypes = [POINTER(c_char), c_short]


# Resume suspended move messages.
BMC_ResumeMoveMessages = lib.BMC_ResumeMoveMessages
BMC_ResumeMoveMessages.restype = c_short
BMC_ResumeMoveMessages.argtypes = [POINTER(c_char), c_short]


# Sets the Analog Monitor Config Parameters.
BMC_SetAnalogMonitorConfigParams = lib.BMC_SetAnalogMonitorConfigParams
BMC_SetAnalogMonitorConfigParams.restype = c_short
BMC_SetAnalogMonitorConfigParams.argtypes = [POINTER(c_char), c_long, c_long, MOD_Monitor_Variable, c_long, c_long]


# Sets the IO Port Config Parameters.
BMC_SetAnalogMonitorConfigParamsBlock = lib.BMC_SetAnalogMonitorConfigParamsBlock
BMC_SetAnalogMonitorConfigParamsBlock.restype = c_short
BMC_SetAnalogMonitorConfigParamsBlock.argtypes = [POINTER(c_char), MOD_AnalogMonitorConfigurationParameters]


# Sets the IO Port Config Parameters.
BMC_SetAuxIOPortConfigParams = lib.BMC_SetAuxIOPortConfigParams
BMC_SetAuxIOPortConfigParams.restype = c_short
BMC_SetAuxIOPortConfigParams.argtypes = [POINTER(c_char), c_long, MOD_AuxIOPortMode, c_long]


# Sets the IO Port Config Parameters.
BMC_SetAuxIOPortConfigParamsBlock = lib.BMC_SetAuxIOPortConfigParamsBlock
BMC_SetAuxIOPortConfigParamsBlock.restype = c_short
BMC_SetAuxIOPortConfigParamsBlock.argtypes = [POINTER(c_char), MOD_AuxIOPortConfigurationSetParameters]


# Sets the backlash distance (used to control hysteresis).
BMC_SetBacklash = lib.BMC_SetBacklash
BMC_SetBacklash.restype = c_short
BMC_SetBacklash.argtypes = [POINTER(c_char), c_short, c_long]


# Sets the current loop parameters for moving to required position.
BMC_SetCurrentLoopParams = lib.BMC_SetCurrentLoopParams
BMC_SetCurrentLoopParams.restype = c_short
BMC_SetCurrentLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessCurrentLoopParameters]


# Sets the digital output bits.
BMC_SetDigitalOutputs = lib.BMC_SetDigitalOutputs
BMC_SetDigitalOutputs.restype = c_short
BMC_SetDigitalOutputs.argtypes = [POINTER(c_char), c_short, c_byte]


# Sets the motor direction sense.
BMC_SetDirection = lib.BMC_SetDirection
BMC_SetDirection.restype = c_short
BMC_SetDirection.argtypes = [POINTER(c_char), c_short, c_bool]


# Sets the electric output parameters.
BMC_SetElectricOutputParams = lib.BMC_SetElectricOutputParams
BMC_SetElectricOutputParams.restype = c_short
BMC_SetElectricOutputParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessElectricOutputParameters]


# Set the Encoder Counter values.
BMC_SetEncoderCounter = lib.BMC_SetEncoderCounter
BMC_SetEncoderCounter.restype = c_short
BMC_SetEncoderCounter.argtypes = [POINTER(c_char), c_short, c_long]


# Set the homing parameters.
BMC_SetHomingParamsBlock = lib.BMC_SetHomingParamsBlock
BMC_SetHomingParamsBlock.restype = c_short
BMC_SetHomingParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_HomingParameters]


# Sets the homing velocity.
BMC_SetHomingVelocity = lib.BMC_SetHomingVelocity
BMC_SetHomingVelocity.restype = c_short
BMC_SetHomingVelocity.argtypes = [POINTER(c_char), c_short, c_uint]


# Sets the IO Port Config Parameters.
BMC_SetIOPortConfigParams = lib.BMC_SetIOPortConfigParams
BMC_SetIOPortConfigParams.restype = c_short
BMC_SetIOPortConfigParams.argtypes = [POINTER(c_char), c_long, MOD_IOPortMode, MOD_IOPortSource]


# Sets the IO Port Config Parameters.
BMC_SetIOPortConfigParamsBlock = lib.BMC_SetIOPortConfigParamsBlock
BMC_SetIOPortConfigParamsBlock.restype = c_short
BMC_SetIOPortConfigParamsBlock.argtypes = [POINTER(c_char), MOD_IOPortConfigurationParameters]


# Sets the jog mode.
BMC_SetJogMode = lib.BMC_SetJogMode
BMC_SetJogMode.restype = c_short
BMC_SetJogMode.argtypes = [POINTER(c_char), c_short, MOT_JogModes, MOT_StopModes]


# Set the jog parameters.
BMC_SetJogParamsBlock = lib.BMC_SetJogParamsBlock
BMC_SetJogParamsBlock.restype = c_short
BMC_SetJogParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_JogParameters]


# Sets the distance to move on jogging.
BMC_SetJogStepSize = lib.BMC_SetJogStepSize
BMC_SetJogStepSize.restype = c_short
BMC_SetJogStepSize.argtypes = [POINTER(c_char), c_short, c_uint]


# Sets jog velocity parameters.
BMC_SetJogVelParams = lib.BMC_SetJogVelParams
BMC_SetJogVelParams.restype = c_short
BMC_SetJogVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


# Sets the joystick parameters.
BMC_SetJoystickParams = lib.BMC_SetJoystickParams
BMC_SetJoystickParams.restype = c_short
BMC_SetJoystickParams.argtypes = [POINTER(c_char), c_short, MOT_JoystickParameters]


# Set the Parameters for Motion from the LCD Display Interface.
BMC_SetLCDMoveParams = lib.BMC_SetLCDMoveParams
BMC_SetLCDMoveParams.restype = c_short
BMC_SetLCDMoveParams.argtypes = [
    POINTER(c_char),
    c_short,
    MOT_JogModes,
    c_int32,
    c_int32,
    c_int32,
    MOT_StopModes,
    c_int32,
    c_int32,
    c_int32]


# Sets the LCD parameters for the device.
BMC_SetLCDMoveParamsBlock = lib.BMC_SetLCDMoveParamsBlock
BMC_SetLCDMoveParamsBlock.restype = c_short
BMC_SetLCDMoveParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_LCDMoveParams]


# Set the LCD Parameters for the Benchtop Display Interface.
BMC_SetLCDParams = lib.BMC_SetLCDParams
BMC_SetLCDParams.restype = c_short
BMC_SetLCDParams.argtypes = [POINTER(c_char), c_int16, c_int16, c_int16, c_int16]


# Sets the LCD parameters for the device.
BMC_SetLCDParamsBlock = lib.BMC_SetLCDParamsBlock
BMC_SetLCDParamsBlock.restype = c_short
BMC_SetLCDParamsBlock.argtypes = [POINTER(c_char), MOT_LCDParams]


# Sets the software limits mode.
BMC_SetLimitsSoftwareApproachPolicy = lib.BMC_SetLimitsSoftwareApproachPolicy
BMC_SetLimitsSoftwareApproachPolicy.restype = c_void_p
BMC_SetLimitsSoftwareApproachPolicy.argtypes = [POINTER(c_char), c_short, MOT_LimitsSoftwareApproachPolicy]


# Set the motor parameters for the Brushless Votor.
BMC_SetMotorParams = lib.BMC_SetMotorParams
BMC_SetMotorParams.restype = c_short
BMC_SetMotorParams.argtypes = [POINTER(c_char), c_short, c_long]


# Set the motor parameters for the Brushless Votor.
BMC_SetMotorParamsExt = lib.BMC_SetMotorParamsExt
BMC_SetMotorParamsExt.restype = c_short
BMC_SetMotorParamsExt.argtypes = [POINTER(c_char), c_short, c_double]


# Sets the absolute minimum and maximum travel range constants for the current stage.
BMC_SetMotorTravelLimits = lib.BMC_SetMotorTravelLimits
BMC_SetMotorTravelLimits.restype = c_short
BMC_SetMotorTravelLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


# Set the motor travel mode.
BMC_SetMotorTravelMode = lib.BMC_SetMotorTravelMode
BMC_SetMotorTravelMode.restype = c_short
BMC_SetMotorTravelMode.argtypes = [POINTER(c_char), c_short, MOT_TravelModes]


# Sets the absolute maximum velocity and acceleration constants for the current stage.
BMC_SetMotorVelocityLimits = lib.BMC_SetMotorVelocityLimits
BMC_SetMotorVelocityLimits.restype = c_short
BMC_SetMotorVelocityLimits.argtypes = [POINTER(c_char), c_short, c_double, c_double]


# Sets the move absolute position.
BMC_SetMoveAbsolutePosition = lib.BMC_SetMoveAbsolutePosition
BMC_SetMoveAbsolutePosition.restype = c_short
BMC_SetMoveAbsolutePosition.argtypes = [POINTER(c_char), c_short, c_int]


# Sets the move relative distance.
BMC_SetMoveRelativeDistance = lib.BMC_SetMoveRelativeDistance
BMC_SetMoveRelativeDistance.restype = c_short
BMC_SetMoveRelativeDistance.argtypes = [POINTER(c_char), c_short, c_int]


# Sets parameters for array of synchronized moves.
BMC_SetMultiChannelMoveArrayParams = lib.BMC_SetMultiChannelMoveArrayParams
BMC_SetMultiChannelMoveArrayParams.restype = c_short
BMC_SetMultiChannelMoveArrayParams.argtypes = [POINTER(c_char), c_long, c_long, c_long, c_long, c_long, c_ulong]


# Sets section of array of synchronized moves.
BMC_SetMultiChannelMoveArraySection = lib.BMC_SetMultiChannelMoveArraySection
BMC_SetMultiChannelMoveArraySection.restype = c_short
BMC_SetMultiChannelMoveArraySection.argtypes = [POINTER(c_char), c_long, c_long, c_long, c_long, c_long]


# Sets the position feedback loop parameters.
BMC_SetPosLoopParams = lib.BMC_SetPosLoopParams
BMC_SetPosLoopParams.restype = c_short
BMC_SetPosLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessPositionLoopParameters]


# Set the Position Counter.
BMC_SetPositionCounter = lib.BMC_SetPositionCounter
BMC_SetPositionCounter.restype = c_short
BMC_SetPositionCounter.argtypes = [POINTER(c_char), c_short, c_long]


# Sets the Position Trigger state.
BMC_SetPositionTriggerState = lib.BMC_SetPositionTriggerState
BMC_SetPositionTriggerState.restype = c_short
BMC_SetPositionTriggerState.argtypes = [POINTER(c_char), c_short, MOT_TriggerState]


# Sets the rack digital output bits.
BMC_SetRackDigitalOutputs = lib.BMC_SetRackDigitalOutputs
BMC_SetRackDigitalOutputs.restype = c_short
BMC_SetRackDigitalOutputs.argtypes = [POINTER(c_char), c_byte]


# Set the Raster Scan Move Parameters .
BMC_SetRasterScanMoveParams = lib.BMC_SetRasterScanMoveParams
BMC_SetRasterScanMoveParams.restype = c_short
BMC_SetRasterScanMoveParams.argtypes = [POINTER(c_char), MOT_RasterScanMoveParams]


# Set the rotation modes for a rotational device.
BMC_SetRotationModes = lib.BMC_SetRotationModes
BMC_SetRotationModes.restype = c_short
BMC_SetRotationModes.argtypes = [POINTER(c_char), c_short, MOT_MovementModes, MOT_MovementDirections]


# Sets the settled current loop parameters for holding at required position.
BMC_SetSettledCurrentLoopParams = lib.BMC_SetSettledCurrentLoopParams
BMC_SetSettledCurrentLoopParams.restype = c_short
BMC_SetSettledCurrentLoopParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessCurrentLoopParameters]


# Sets the stage axis position limits.
BMC_SetStageAxisLimits = lib.BMC_SetStageAxisLimits
BMC_SetStageAxisLimits.restype = c_short
BMC_SetStageAxisLimits.argtypes = [POINTER(c_char), c_short, c_int, c_int]


# Sets the track settled parameters used to decide when settled at right position.
BMC_SetTrackSettleParams = lib.BMC_SetTrackSettleParams
BMC_SetTrackSettleParams.restype = c_short
BMC_SetTrackSettleParams.argtypes = [POINTER(c_char), c_short, MOT_BrushlessTrackSettleParameters]


# Sets the IO Trigger Config Parameters.
BMC_SetTriggerIOConfigParams = lib.BMC_SetTriggerIOConfigParams
BMC_SetTriggerIOConfigParams.restype = c_short
BMC_SetTriggerIOConfigParams.argtypes = [
    POINTER(c_char),
    c_short,
    MOT_TriggerInputConfigModes,
    MOT_TriggerPolarity,
    MOT_TriggerInputSource,
    MOT_TriggerOutputConfigModes,
    MOT_TriggerPolarity,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long,
    c_long]


# Sets the IO Trigger Config Parameters.
BMC_SetTriggerIOConfigParamsBlock = lib.BMC_SetTriggerIOConfigParamsBlock
BMC_SetTriggerIOConfigParamsBlock.restype = c_short
BMC_SetTriggerIOConfigParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_TriggerIOConfigParameters]


# Sets the trigger switch bits.
BMC_SetTriggerSwitches = lib.BMC_SetTriggerSwitches
BMC_SetTriggerSwitches.restype = c_short
BMC_SetTriggerSwitches.argtypes = [POINTER(c_char), c_short, c_byte]


# Sets the move velocity parameters.
BMC_SetVelParams = lib.BMC_SetVelParams
BMC_SetVelParams.restype = c_short
BMC_SetVelParams.argtypes = [POINTER(c_char), c_short, c_int, c_int]


# Set the move velocity parameters.
BMC_SetVelParamsBlock = lib.BMC_SetVelParamsBlock
BMC_SetVelParamsBlock.restype = c_short
BMC_SetVelParamsBlock.argtypes = [POINTER(c_char), c_short, MOT_VelocityParameters]


# Sets the velocity profile parameters.
BMC_SetVelocityProfileParams = lib.BMC_SetVelocityProfileParams
BMC_SetVelocityProfileParams.restype = c_short
BMC_SetVelocityProfileParams.argtypes = [POINTER(c_char), c_short, MOT_VelocityProfileParameters]


# Starts array of synchronized moves.
BMC_StartMultiChannelMoveArray = lib.BMC_StartMultiChannelMoveArray
BMC_StartMultiChannelMoveArray.restype = c_short
BMC_StartMultiChannelMoveArray.argtypes = [POINTER(c_char), c_long, c_ulong]


# Starts the internal polling loop which continuously requests position and status.
BMC_StartPolling = lib.BMC_StartPolling
BMC_StartPolling.restype = c_bool
BMC_StartPolling.argtypes = [POINTER(c_char), c_short, c_int]


# Stop the current move immediately (with risk of losing track of position).
BMC_StopImmediate = lib.BMC_StopImmediate
BMC_StopImmediate.restype = c_short
BMC_StopImmediate.argtypes = [POINTER(c_char), c_short]


# Stop the current vector move immediately (with risk of losing track of position).
BMC_StopImmediateSynchronously = lib.BMC_StopImmediateSynchronously
BMC_StopImmediateSynchronously.restype = c_short
BMC_StopImmediateSynchronously.argtypes = [POINTER(c_char), c_ulong]


# Stops the internal polling loop.
BMC_StopPolling = lib.BMC_StopPolling
BMC_StopPolling.restype = c_void_p
BMC_StopPolling.argtypes = [POINTER(c_char), c_short]


# Stop the current move using the current velocity profile.
BMC_StopProfiled = lib.BMC_StopProfiled
BMC_StopProfiled.restype = c_short
BMC_StopProfiled.argtypes = [POINTER(c_char), c_short]


# Stop the current vector move using the current velocity profile.
BMC_StopProfiledSynchronously = lib.BMC_StopProfiledSynchronously
BMC_StopProfiledSynchronously.restype = c_short
BMC_StopProfiledSynchronously.argtypes = [POINTER(c_char), c_ulong]


# Suspend automatic messages at ends of moves.
BMC_SuspendMoveMessages = lib.BMC_SuspendMoveMessages
BMC_SuspendMoveMessages.restype = c_short
BMC_SuspendMoveMessages.argtypes = [POINTER(c_char), c_short]


# Gets the time in milliseconds since tha last message was received from the device.
BMC_TimeSinceLastMsgReceived = lib.BMC_TimeSinceLastMsgReceived
BMC_TimeSinceLastMsgReceived.restype = c_bool
BMC_TimeSinceLastMsgReceived.argtypes = [POINTER(c_char), c_short, c_int64]


# Move selected channels to the specified positions synchronously.
BMC_VectorMoveToPosition = lib.BMC_VectorMoveToPosition
BMC_VectorMoveToPosition.restype = c_short
BMC_VectorMoveToPosition.argtypes = [POINTER(c_char), MOT_ChannelPosition, c_int, c_int, c_int]


# Wait for next MessageQueue item.
BMC_WaitForMessage = lib.BMC_WaitForMessage
BMC_WaitForMessage.restype = c_bool
BMC_WaitForMessage.argtypes = [POINTER(c_char), c_short, c_long, c_long, c_ulong]


# Creates a manual device configuration entry.
TLI_CreateManualDeviceEntry = lib.TLI_CreateManualDeviceEntry
TLI_CreateManualDeviceEntry.restype = c_short
TLI_CreateManualDeviceEntry.argtypes = [POINTER(c_char)]


# Deletes a manual device configuration entry.
TLI_DeleteManualDeviceEntry = lib.TLI_DeleteManualDeviceEntry
TLI_DeleteManualDeviceEntry.restype = c_short
TLI_DeleteManualDeviceEntry.argtypes = [POINTER(c_char)]


# Get the device information from the USB port.
TLI_GetDeviceInfo = lib.TLI_GetDeviceInfo
TLI_GetDeviceInfo.restype = c_short
TLI_GetDeviceInfo.argtypes = [POINTER(c_char), POINTER(c_char), TLI_DeviceInfo]


# Get the entire contents of the device list.
TLI_GetDeviceList = lib.TLI_GetDeviceList
TLI_GetDeviceList.restype = c_short
TLI_GetDeviceList.argtypes = [SafeArray]


# Get the contents of the device list which match the supplied typeID.
TLI_GetDeviceListByType = lib.TLI_GetDeviceListByType
TLI_GetDeviceListByType.restype = c_short
TLI_GetDeviceListByType.argtypes = [SafeArray, c_int]


# Get the contents of the device list which match the supplied typeID.
TLI_GetDeviceListByTypeExt = lib.TLI_GetDeviceListByTypeExt
TLI_GetDeviceListByTypeExt.restype = c_short
TLI_GetDeviceListByTypeExt.argtypes = [POINTER(c_char), c_ulong, c_int]


# Get the contents of the device list which match the supplied typeIDs.
TLI_GetDeviceListByTypes = lib.TLI_GetDeviceListByTypes
TLI_GetDeviceListByTypes.restype = c_short
TLI_GetDeviceListByTypes.argtypes = [SafeArray, c_int, c_int]


# Get the contents of the device list which match the supplied typeIDs.
TLI_GetDeviceListByTypesExt = lib.TLI_GetDeviceListByTypesExt
TLI_GetDeviceListByTypesExt.restype = c_short
TLI_GetDeviceListByTypesExt.argtypes = [POINTER(c_char), c_ulong, c_int, c_int]


# Get the entire contents of the device list.
TLI_GetDeviceListExt = lib.TLI_GetDeviceListExt
TLI_GetDeviceListExt.restype = c_short
TLI_GetDeviceListExt.argtypes = [POINTER(c_char), c_ulong]


# Gets the device list size.
TLI_GetDeviceListSize = lib.TLI_GetDeviceListSize
TLI_GetDeviceListSize.restype = c_short
TLI_GetDeviceListSize.argtypes = []


# Scans a range of addresses and returns a list of the ip addresses of Thorlabs devices found.
TLI_ScanEthernetRange = lib.TLI_ScanEthernetRange
TLI_ScanEthernetRange.restype = c_short
TLI_ScanEthernetRange.argtypes = [POINTER(c_char), POINTER(c_char), c_int, c_int, POINTER(c_char), c_ulong]


# Uninitialize a connection to the Simulation Manager, which must already be running.
TLI_UninitializeSimulations = lib.TLI_UninitializeSimulations
TLI_UninitializeSimulations.restype = c_void_p
TLI_UninitializeSimulations.argtypes = []
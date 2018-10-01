MIN_TIMEOUT = 100    # minimum possible timeout
MAX_TIMEOUT = 10000  # maximum possible timeout

class TimeoutCalculator:
  """
  Timeout Calculator maintains the mean RTT and RTT variance. Data members of this class
  include alpha, beta and K (which have the same meaning as discussed in the lectures)
  """
  def __init__(self):
    self.mean_rtt      = 0.0
    self.rtt_var       = 0.0
    self.alpha         = 0.125       # alpha value for mean_rtt's EWMA
    self.beta          = 0.25        # beta value for rtt_var's EWMA
    self.k             = 4.0         # what multiple of RTT variation to use in the timeout
    # TODO: Initialize the variable self.timeout to the minimum possible value
    self.ewma_init     = False       # EWMA is not initialized until the first sample is seen
  def update_timeout(self, rtt_sample):
    """
    This function is used to update the mean and variance RTTs
    """
    if (not self.ewma_init): # If you have seen no rtts yet or exponentially backed off before
      pass
      # TODO: Initialize mean_rtt to current sample
      # TODO: Initialize rtt_var to half of current sample
      # TODO: Set timeout using mean_rtt and rtt_var
      # TODO: Remember to update self.ewma_init correctly so that the else branch is taken on subsequent packets.
    else:
      pass
      # TODO: Update rtt var based on rtt_sample and old mean rtt
      # TODO: Update mean rtt based on rtt_sample
      # TODO: Update timeout based on mean rtt and rtt var

    # TODO: Before you return from this function,
    # ensure that updated timeout is between MIN_TIMEOUT and MAX_TIMEOUT
    # i.e, if your timeout is above MAX_TIMEOUT, you should set it to MAX_TIMEOUT.
    # and  if it's below MIN_TIMEOUT, you should set it to MIN_TIMEOUT
    
  def exp_backoff(self):
    """
    This function is used to double the timeout representing an exponential backoff
    """
    pass
    # TODO: Exponentially back off by doubling the timeout
    # TODO: Re-initialize the EWMA
    print ("exponential backoff here, re-initializing EWMA")
    # TODO: Before you return from this function,
    # ensure that updated timeout is between MIN_TIMEOUT and MAX_TIMEOUT
    # i.e, if your timeout is above MAX_TIMEOUT, you should set it to MAX_TIMEOUT.
    # and  if it's below MIN_TIMEOUT, you should set it to MIN_TIMEOUT
    return self.timeout

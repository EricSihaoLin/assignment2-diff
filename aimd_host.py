import sys
from packet import *
from timeout_calculator  import *

class UnackedPacket:
  """
  Structure to store information associated with an unacked packet
  so that we can maintain a list of such UnackedPacket objects
  
  Data members of this class include

  seq_num:  Sequence number of the unacked packet

  num_retx: Number of times this packet has been retransmitted so far

  timeout_duration: Timeout duration for this packet

  timeout_tick: The time (in ticks) at which the packet timeout

  """

  def __init__(self, seq_num):
    """
    Constructor for UnackedPacket. This sets the default values for class data members

    """
    self.seq_num      = seq_num # sequence number of unacked packet
    self.num_retx     = 0       # how many times it's been retransmitted so far
    self.timeout_duration = 0   # what is the duration of its timeout
    self.timeout_tick     = 0   # at what tick does this packet timeout?

  def __str__(self):
    """
    String representation of unacked packet for debugging

    """
    return str(self.seq_num)

class AimdHost:
  """
  This class implements a host that follows the AIMD protocol.
  Data members of this class are

  **unacked**: List of unacked packets

  **window**: Size of the window at any given moment

  **max_seq**: Maximum sequence number sent so far

  **in_order_rx_seq**: Maximum sequence number received so far

  **slow_start**: Boolean to indicate whether algorithm is in slow start or not

  **next_decrease**: Time (in ticks) at which the window size should be descreased

  **timeout_calculator**: An object of class TimeoutCalculator
  (Refer to TimeoutCalculator class for more information)
    
  There are two member functions - send and recv that perform the task of sending
  and receiving packets respectively. All send and receive logic should be written
  within one of these two functions.

  """
  def __init__(self):
    self.unacked = []           # list of unacked packets
    self.window = 1             # We'll initialize window to 1
    self.max_seq = -1           # maximum sequence number sent so far
    self.in_order_rx_seq = -1   # maximum sequence number received so far in order
    self.slow_start = True      # Are we in slow start?
    self.next_decrease = -1     # When to next decrease your window; adds some hystersis
    self.timeout_calculator = TimeoutCalculator() # object for computing timeouts

  def send(self, tick):
    """
    Function to send packet on to the network. Host should first retransmit any
    Unacked packets that have timed out. Host should also descrease the window size
    if it is time for the next decrease. After attempting retransmissions, if the window
    is not full, fill up the window with new packets.
    
    Args:

        **tick**: Simulated time

    Returns:
        
        A list of packets that the host wants to transmit on to the network
    """
    # TODO: Create an empty list of packets that the host will send

    # First, process retransmissions
    for i in range(0, len(self.unacked)):
      unacked_pkt = self.unacked[i]
      if (tick >= unacked_pkt.timeout_tick):
        pass
        # TODO: Retransmit any packet that has timed out
        # by doing the following in order
        # (1) creating a new packet,
        # (2) setting its retx attribute to True (just for debugging)
        # (3) Append the packet to the list of packets created earlier
        # (4) Backing off the timer
        # (5) Updating timeout_tick and timeout_duration appropriately after backing off the timer
        # (6) Updating num_retx

        # TODO: Multiplicative decrease, if it's time for the next decrease
        # Cut window by half, but don't let it go below 1
        # TODO: Make sure the next multiplicative decrease doesn't happen until an RTT later
        # (use the timeout_calculator to estimate the RTT)

        # Exit slow start, whether you were in it or not
        self.slow_start = False

      self.unacked[i] = unacked_pkt

    # Now fill up the window with new packets
    while (len(self.unacked) < self.window):
      pass
      # TODO: Create new packets, set their retransmission timeout, and transmit them
      # TODO: Remember to update self.max_seq and add the just sent packet to self.unacked

  def recv(self, pkt, tick):
    """
    Function to get a packet from the network.

    Args:
        
        **pkt**: Packet received from the network

        **tick**: Simulated time
    """
    assert(tick > pkt.sent_ts)
    pass
    # TODO: Compute RTT sample
    # TODO: Update timeout

    # TODO: Remove received packet from self.unacked

    # TODO: Update in_order_rx_seq to reflect the largest sequence number that you
    # have received in order so far

    # TODO: Increase your window on this ACK based on whether you are in slow start or not
    # TODO: Remember this function is called on every ACK (not every RTT),
    # so you should adjust your window accordingly.

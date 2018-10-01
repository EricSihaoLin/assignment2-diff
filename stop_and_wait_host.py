from packet import *
from timeout_calculator  import *  # Import timeout calculator for StopAndWait

class StopAndWaitHost:
  """
  This host implements the stop and wait protocol. Here the host only
  sends one packet in return of an acknowledgement.
  """
  def __init__(self):
    self.in_order_rx_seq = -1      # maximum sequence number received so far in order
    self.ready_to_send = True      # can we send a packet or are we still waiting for an ACK?
    self.packet_sent_time   = -1   # when was this packet sent out last?
    self.timeout_calculator = TimeoutCalculator() # initialize TimeoutCalculator

  def send(self, tick):
    """
    Function to send a packet with the next sequence number on to the network.
    """
    if (self.ready_to_send):
      pass
      # TODO: Send next sequence number by creating a packet
      # TODO: Remember to update packet_sent_time and ready_to_send appropriately
      # TODO: Return the packet
    elif (tick - self.packet_sent_time >= self.timeout_calculator.timeout):
      pass
      # TODO: Timeout has been exceeded, retransmit packet
      # following the same procedure as above when transmitting a packet for the first time
      # TODO: Exponentially back off the timer
      # TODO: Set retx field on packet to detect retransmissions for debugging
      # TODO: Return the packet

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
    # TODO: Update timeout based on RTT sample

    # TODO: Update self.in_order_rx_seq and self.ready_to_send depending on pkt.seq_num

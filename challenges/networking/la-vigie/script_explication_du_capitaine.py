import string

from scapy.all import IP, TCP, UDP, Raw, DNS, DNSQR, DNSRR, wrpcap
import random


random.seed(1337)

# Craft an IP packet
ip_header_send = IP(src="192.168.1.2", dst="185.199.108.153")
ip_header_recv = IP(src="185.199.108.153", dst="192.168.1.2")

hostname = "www.unitedctf.ca"
dns_query = DNS(id=random.randint(0, 65535), qr=0, qdcount=1, ancount=0, nscount=0, arcount=0,
                    qd=DNSQR(qname=hostname, qtype="A", qclass="IN"))
dns_response = DNS(id=dns_query.id, qr=1, aa=1, ancount=1, qd=dns_query.qd, an=DNSRR(rrname=dns_query.qd.qname,
                                                                                     type=1, ttl=600, rdata="185.199.108.153"))
# Include the DNS query packet
dns_packets = [IP(src="192.168.1.2", dst="192.168.0.1") / UDP(sport=12345, dport=53) / dns_query, IP(src="192.168.0.1", dst="192.168.1.2") / UDP(sport=53, dport=12345) / dns_response]
def threeWayHS():
    # Choose a random source port (sport)
    sport = random.randint(1024, 65535)

    # Craft a TCP SYN segment
    seq_s = random.randint(1000, 9999)
    dport = 80
    tcp_syn_segment = TCP(sport=sport, dport=dport, flags="S", seq=seq_s)

    # Combine the packet components for the initial SYN
    syn_packet = ip_header_send / tcp_syn_segment

    # Calculate the values needed to continue the conversation
    seq_d = random.randint(1000, 9999)

    # Craft a TCP SYN-ACK segment for the response
    tcp_syn_ack_segment = TCP(sport=dport, dport=sport, flags="SA", seq=seq_d, ack=seq_s + 1)

    # Combine the packet components for the SYN-ACK
    syn_ack_packet = ip_header_recv / tcp_syn_ack_segment

    # Craft a TCP ACK segment to complete the handshake
    seq_s += 1
    tcp_ack_segment = TCP(sport=sport, dport=dport, flags="A", seq=seq_s, ack=seq_d + 1)

    # Combine the packet components for the final ACK
    ack_packet = ip_header_send / tcp_ack_segment

    return sport, dport, seq_s, seq_d + 1, [syn_packet, syn_ack_packet, ack_packet]


def finTcp(sport, dport, seq_s, seq_d):
    # Create a TCP FIN segment to close the connection
    tcp_fin_segment = TCP(sport=sport, dport=dport, flags="F", seq=seq_d, ack=seq_s + 1)

    # Combine the packet components for the FIN packet
    fin_packet = ip_header_recv / tcp_fin_segment


    return [fin_packet]


def tcp_ip_packet(iph, seq, ack, flags, src_port, dst_port):
    return iph / TCP(sport=src_port, dport=dst_port, seq=seq, ack=ack, flags=flags)


def noise(seq, ack, src_port, dst_port):
    return tcp_ip_packet(ip_header_recv, ack, seq, "A", dst_port, src_port) / Raw(
        load="This is just some noise to make the challenge a bit harder.")


def ack_pac(seq, ack, src_port, dst_port):
    return tcp_ip_packet(ip_header_send, seq, ack, "A", src_port, dst_port)


if __name__ == '__main__':
    sport, dport, seq_s, seq_d, TWHS_packet = threeWayHS()

    noise_packets = []
    for _ in range(6):
        noise_packets.append(noise(seq_s, seq_d, sport, dport))
        seq_d += 59
        noise_packets.append(ack_pac(seq_s, seq_d, sport, dport))

    noise_packets.append(tcp_ip_packet(ip_header_recv, seq_d, seq_s, "A", dport, sport) / Raw(load="flag-Iswe4rTh3sh4rkT4lkEdT0m3"))
    seq_d += 29
    noise_packets.append(ack_pac(seq_s, seq_d, sport, dport))

    for _ in range(4):
        noise_packets.append(noise(seq_s, seq_d, sport, dport))
        seq_d += 59
        noise_packets.append(ack_pac(seq_s, seq_d, sport, dport))

    fin_packet = finTcp(sport, dport, seq_s, seq_d)
    wrpcap("explication-du-capitaine.pcap", dns_packets + TWHS_packet + noise_packets + fin_packet + [ack_pac(seq_s, 1, sport, dport)])
    print("Packets added to explication-du-capitaine-1.pcap")

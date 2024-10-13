
# Pub/Sub Middleware

This project implements a Publish/Subscribe (Pub/Sub) middleware using client-server socket programming. The middleware enables asynchronous communication between multiple publishers and subscribers, allowing message exchanges based on topics.

## Features

- Supports multiple concurrent client connections.
- Clients can act as publishers or subscribers.
- Topic-based message filtering between publishers and subscribers.
- CLI-based interaction between the server and clients.
- Graceful client disconnection on the "terminate" command.

## How It Works

1. **Server**:
   - Listens for connections on a predefined port.
   - Handles multiple client connections (publishers and subscribers).
   - Routes messages from publishers to subscribers based on specified topics.

2. **Clients**:
   - Connect to the server by specifying the server's IP, port, role (publisher/subscriber), and topic.
   - Publishers send messages on specific topics.
   - Subscribers receive messages on the topics they are subscribed to.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/downloads/) or another supported language (C/C++, Java).
- Basic understanding of socket programming.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pubsub-middleware.git
   ```

2. Navigate to the project directory:

   ```bash
   cd pubsub-middleware
   ```

### Usage

1. **Start the server**:

   ```bash
   python server.py <PORT>
   ```

2. **Start a client as a publisher**:

   ```bash
   python client.py <SERVER_IP> <PORT> PUBLISHER <TOPIC>
   ```

3. **Start a client as a subscriber**:

   ```bash
   python client.py <SERVER_IP> <PORT> SUBSCRIBER <TOPIC>
   ```

### Example

1. Start the server:

   ```bash
   python server.py 5000
   ```

2. Connect a client as a publisher:

   ```bash
   python client.py 192.168.1.1 5000 PUBLISHER sports
   ```

3. Connect a client as a subscriber:

   ```bash
   python client.py 192.168.1.1 5000 SUBSCRIBER sports
   ```

The publisher's messages will be received by all subscribers of the "sports" topic.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

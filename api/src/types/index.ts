export interface ServerToClientEvents {
    clientJoin: (args: { id: string }) => void;
    clientLeave: (args: { id: string }) => void;
}

export interface ClientToServerEvents {
    keyPress: (args: { key: string, sid: string }) => void;
}

export interface InterServerEvents {

}

export interface SocketData {

} 
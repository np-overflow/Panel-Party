export interface ServerToClientEvents {
    clientJoin: (args: { id: string, pid: string }) => void;
    clientLeave: (args: { id: string }) => void;
    keyPress: (args: { key: string, id: string }) => void;
}

export interface ClientToServerEvents {
    keyPress: (args: { key: string, sid: string }) => void;
}

export interface InterServerEvents {

}

export interface SocketData {

} 
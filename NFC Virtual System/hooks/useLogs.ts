import { useState } from 'react';

let globalLogs: any[] = [];

export default function useLogs() {
  const [logs, setLogs] = useState(globalLogs);

  const addLog = (status: string) => {
    const newLog = {
      id: Date.now().toString(),
      status,
      time: new Date().toLocaleTimeString()
    };

    globalLogs = [newLog, ...globalLogs];
    setLogs([...globalLogs]);
  };

  return { logs, addLog };
}
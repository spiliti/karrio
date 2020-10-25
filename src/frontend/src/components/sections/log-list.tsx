import React, { MouseEventHandler } from 'react';
import { View } from '@/library/types';
import StatusCode from '@/components/status-code-badge';
import { Log, PaginatedLogs, state } from '@/library/api';

interface LogListView extends View {
    logs?: PaginatedLogs;
    handleLogSelection: (log: Log) => MouseEventHandler;
}

const LogList: React.FC<LogListView> = ({ handleLogSelection, logs }) => {
    const getLogs = (url?: string | null) => async (_: React.MouseEvent) => {
        await state.fetchLogs(url as string);
    };

    return (
        <>

            <nav className="breadcrumb has-succeeds-separator" aria-label="breadcrumbs">
                <ul>
                    <li className="is-active"><a href="#" aria-current="page">Logs</a></li>
                </ul>
            </nav>

            <div className="table-container">
                <table className="table is-fullwidth is-hoverable is-size-7">

                    <thead className="logs-table">
                        <tr>
                            <th className="status"><span className="ml-2">STATUS</span></th>
                            <th className="description">DESCRIPTION</th>
                            <th className="date has-text-right"><span className="mr-2">DATE</span></th>
                        </tr>
                    </thead>

                    <tbody>
                        {logs?.results.map((log) => (

                            <tr key={log.id} onClick={handleLogSelection(log)}>
                                <td className="status"><StatusCode code={log.status_code} /></td>
                                <td className="description">{`${log.method} ${log.path}`}</td>
                                <td className="date has-text-right">
                                    <span className="mr-2">{formatDate(log.requested_at)}</span>
                                </td>
                            </tr>

                        ))}
                    </tbody>

                </table>
            </div>

            <footer className="px-2 py-2 is-vcentered">
                <div className="buttons is-centered">
                    <button className="button is-small" onClick={getLogs(logs?.previous)} disabled={logs?.previous === null}>
                        Previous
                    </button>
                    <button className="button is-small" onClick={getLogs(logs?.next)} disabled={logs?.next === null}>
                        Next
                    </button>
                </div>
            </footer>

        </>
    );
}

export function formatDate(date_string: string): string {
    const date = new Date(date_string);
    let [month, day, year] = date.toLocaleDateString().split("/");
    let [hour, minute, second] = date.toLocaleTimeString().split(/:| /);
    return `${day}/${month}/${year}, ${hour}:${minute}:${second}`;
}

export default LogList;

export interface IQueueInfo {
    status: number;
    data: {
        error: string | null;
        cabinetList: IQueueInfoRow[];
    };
};

export interface IQueueInfoRow {
    name: string;
    number: number;
    playerCount: number;
    maxCapacity: number;
    updateTime: string;
};

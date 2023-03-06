export interface IQueueInfo {
    maxCapacity: number;
    cabinets: {
        left: IQueueInfoRow;
        right: IQueueInfoRow;
    };
};

export interface IQueueInfoRow {
    count: number;
    updateTime: string | Date;
};

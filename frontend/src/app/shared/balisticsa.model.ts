import { ArrayType } from "@angular/compiler";

export interface APIView{
    count: number;
    next: string;
    previous: string;
    results: Array<any>;
}

export interface SootingView {
    owner: string;
    wepon: string;
    date_Shooting: string;
    ammo: string;
    document: string;
    safe_number: string
}

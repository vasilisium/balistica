import { ArrayType } from "@angular/compiler";

export interface APIView{
    count: number;
    next: string;
    previous: string;
    results: Array<any>;
}

export interface PersonNameView {
    id: number;
    first_name: string;
    second_name: string;
    last_name: string;
    date_created: Date;
}

export interface WeponView {
    id: number;
    owner: PersonNameView;
    brand: string;
    model: string;
    calibre: string;
    serial_number: string;
    date_created: Date;
}

export interface AmmoView {
    id: number;
    description: string;
}

export interface SootingView {
    id: number;
    wepon: WeponView;
    date_Shooting: string;
    ammo: AmmoView;
    document: string;
    safe_number: string
}

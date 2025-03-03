import { requestGet, requestPost } from '@/utils/request'
import type { Existence, Metadata, Side } from '@/utils/datatypes'
import { da } from 'vuetify/locale';

const BACKEND_URL = import.meta.env.VITE_BACKEND_URL

export default class Caller {
    private lastLoaded: number;

    constructor() {
        this.lastLoaded = 0;
    }

    async isNextAvailable(): Promise<Existence> {
        const oldId = this.lastLoaded;
        const data = await requestGet<Existence>(BACKEND_URL + `/is_next_available/${oldId}`)
        if (data.exists) {
            this.lastLoaded = data.imgId;
        }
        return data
    }

    async getMetadata(side: Side, imgId: number): Promise<Metadata> {
        return await requestGet<Metadata>(BACKEND_URL + `/get_metadata/${side}/${imgId}`)
    }

    async processSelected(pairList: number[]) {
        return await requestPost<undefined>(BACKEND_URL + '/process_selected', {selectedIds: pairList})
    }
    
    getImageUrl(side: Side, imgId: number, imgType?: string): string {
        let baseUrl = `${BACKEND_URL}/get_image/${side}/${imgId}`;

        if (typeof imgType !== 'undefined') {
            return baseUrl
        }

        return baseUrl + `?type=${imgType}`
      }
    
    getImageUid(side: Side, imgId: number): string {
        return `${imgId}${side}`
    }
};
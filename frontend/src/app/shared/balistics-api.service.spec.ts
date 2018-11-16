import { TestBed } from '@angular/core/testing';

import { BalisticsAPIService } from './balistics-api.service';

describe('BalisticsAPIService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: BalisticsAPIService = TestBed.get(BalisticsAPIService);
    expect(service).toBeTruthy();
  });
});

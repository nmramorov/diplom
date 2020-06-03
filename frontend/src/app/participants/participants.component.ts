import { Component, OnInit } from '@angular/core';

import {Participant} from '../../../participant';
import {ParticipantService} from '../participant.service';
import {Sheet} from '../../../sheet';
import {SheetService} from "../sheet.service";
import {ActivatedRoute} from "@angular/router";
import {Location} from "@angular/common";
import {tap} from "rxjs/operators";

@Component({
  selector: 'app-participants',
  templateUrl: './participants.component.html',
  styleUrls: ['./participants.component.css']
})
export class ParticipantsComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private participantService: ParticipantService,
    private location: Location,
    private sheetService: SheetService
  ) { }

  participants: Participant[];
  sheet: Sheet;

  getCurrentSheet(): string {
    return this.sheet.sheet;
  }

  getSheet(): void {
    const identifier = +this.route.snapshot.paramMap.get('identifier');
    this.sheetService.getSheet(identifier)
      .subscribe(
        sheet => this.sheet = sheet);
  }

  goBack(): void {
    this.location.back();
  }

  ngOnInit(): void {
    this.getSheet();
  }

}

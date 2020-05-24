import { Component, OnInit } from '@angular/core';

import {PARTICIPANTS} from '../mock-participants';
import {Participant} from '../../../participant';

@Component({
  selector: 'app-participants',
  templateUrl: './participants.component.html',
  styleUrls: ['./participants.component.css']
})
export class ParticipantsComponent implements OnInit {

  constructor() { }

  participants = PARTICIPANTS;
  selectedParticipant: Participant;

  onSelect(participant: Participant): void {
    this.selectedParticipant = participant;
  }

  ngOnInit(): void {
  }

}

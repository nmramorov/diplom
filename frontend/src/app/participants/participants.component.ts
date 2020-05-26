import { Component, OnInit } from '@angular/core';

import {PARTICIPANTS} from '../mock-participants';
import {Participant} from '../../../participant';
import {ParticipantService} from '../participant.service';

@Component({
  selector: 'app-participants',
  templateUrl: './participants.component.html',
  styleUrls: ['./participants.component.css']
})
export class ParticipantsComponent implements OnInit {

  constructor(private participantService: ParticipantService) { }

  participants: Participant[];
  selectedParticipant: Participant;

  onSelect(participant: Participant): void {
    this.selectedParticipant = participant;
  }

  getParticipants(): void {
    this.participantService.getParticipants()
      .subscribe(participants => this.participants = participants);
  }

  ngOnInit(): void {
    this.getParticipants();
  }

}

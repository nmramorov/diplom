import { Component, OnInit } from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import { Participant} from '../../../participant';
import {ParticipantService} from '../participant.service';
import {Location} from '@angular/common';

@Component({
  selector: 'app-participant-detail',
  templateUrl: './participant-detail.component.html',
  styleUrls: ['./participant-detail.component.css']
})
export class ParticipantDetailComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private participantService: ParticipantService,
    private location: Location
  ) { }

  participant: Participant;

  ngOnInit(): void {
    this.getParticipant();
}

  getParticipant(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.participantService.getParticipant(id)
      .subscribe(participant => this.participant = participant);
  }

  goBack(): void {
    this.location.back();
  }
}

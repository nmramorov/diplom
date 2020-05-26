import { Component, OnInit, Input } from '@angular/core';
import { ParticipantService } from '../participant.service';
import { Participant} from '../../../participant';

@Component({
  selector: 'app-participant-detail',
  templateUrl: './participant-detail.component.html',
  styleUrls: ['./participant-detail.component.css']
})
export class ParticipantDetailComponent implements OnInit {

  constructor() { }

  @Input()participant: Participant;

  ngOnInit(): void {
  }
}

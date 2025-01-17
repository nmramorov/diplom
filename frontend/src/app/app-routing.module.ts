import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {ParticipantsComponent} from './participants/participants.component';
import {ParticipantDetailComponent} from './participant-detail/participant-detail.component';
import { DashboardComponent } from './dashboard/dashboard.component';

const routes: Routes = [
  { path: 'participants/:identifier', component: ParticipantsComponent },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'participants/:identifier/detail/:identifier', component: ParticipantDetailComponent},
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }

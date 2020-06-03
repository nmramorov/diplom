import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import {HttpClientModule, HttpHeaders} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { ParticipantsComponent } from './participants/participants.component';
import { ParticipantDetailComponent } from './participant-detail/participant-detail.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ParticipantListComponent } from './participant-list/participant-list.component';

@NgModule({
  declarations: [
    AppComponent,
    ParticipantsComponent,
    ParticipantDetailComponent,
    DashboardComponent,
    ParticipantListComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    AppRoutingModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {Credit} from './credit_display.model';
import {CreditApiService} from './credit_display-api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  creditsListSubs: Subscription;
  creditsList: Credit[];

  constructor(private creditApi: CreditApiService) {
  }

  ngOnInit() {
    this.creditsListSubs = this.creditApi
      .getCredits()
      .subscribe(res => {
          this.creditsList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.creditsListSubs.unsubscribe();
  }
}

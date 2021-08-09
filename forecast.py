# Copyright 2017 Google, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Forecast(object):
    def __init__(self,args):
        #if args > 2
        if(len(args) > 2):
            self.postcode = args[0]
            localities = [{
                'locality' : args[1],
                'forecasts' : [{
                    'forecastDate' : args[2],
                    'minTemperature' : args[3],
                    'maxTemperature' : args[4]
                }]
            }]
            self.localities = localities
        else:
            self.postcode = args[0]
            self.localities = args[1]

    def has_locality(self, locality):
        if self.localities == None:
            return False
        for x in self.localities:
            if x['locality'] == locality:
                return True
        return False
    
    def add_locality(self, locality, forecastDate, minTemperature, maxTemperature):
        #locality exists
        
        for idx, val in enumerate(self.localities):
            if val[u'locality'] == locality:
                self.localities[idx]['forecasts'].append({
                    'forecastDate':forecastDate, 
                    'minTemperature': minTemperature,
                    'maxTemperature':maxTemperature})
                return
        #new locality
        newLocality = { 
            'locality' : locality,
            'forecasts': [{
                'forecastDate' : forecastDate,
                'minTemperature' : minTemperature,
                'maxTemperature' : maxTemperature
            }]
        }
        self.localities.append(newLocality)
    
    def to_dict(self):
        dest = {"postcode": self.postcode}
        if self.localities:
            dest["localities"] = self.localities
        return dest
              
    @staticmethod
    def from_dict(source):
        print(source)
        # [START_EXCLUDE]
        forecast = Forecast([ 
            source['postcode'], 
            source['localities']])

        return forecast
        # [END_EXCLUDE]
   
    def __repr__(self):
        return f"Postcode(\
                postcode={self.postcode}, \
                localities={self.localities}\
            )"


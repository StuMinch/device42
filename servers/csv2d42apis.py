'''
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''

############################################################################################
# csv file to api helper utility v2.1 that uploads data to device42 via REST APIs
# step 1: create csv file, comma separated, header row must match the arguments for the API call.
# step 2: Change lines 26-31
# step 3: Execute the script
############################################################################################
import types
import urllib2
import urllib
import base64
import csv

##### Change Following lines to match your environment #####
### API URLS available at http://docs.device42.com/apis/ ###

D42_DEVICE_API_URL = 'https://10.100.0.114/api/device/'  #make sure to end in /
D42_IP_API_URL = 'https://10.100.0.114/api/ip/'
D42_USERNAME = 'username'
D42_PASSWORD = 'password'
API_METHOD = 'post'                                                          #whether you are doing a put or post call.
CSV_FILE_NAME = 'some_file.csv'                                             #name of the file with the values being uploaded
DEBUG = True                                                                #True or False. True for detailed info per call

def post(params):
    data= urllib.urlencode(params)
    headers = {
            'Authorization' : 'Basic '+ base64.b64encode(D42_USERNAME + ':' + D42_PASSWORD),
            'Content-Type' : 'application/x-www-form-urlencoded'
        }
    req = urllib2.Request(D42_DEVICE_API_URL, data, headers)
    if DEBUG: print '---REQUEST---',req.get_full_url()
    if DEBUG: print req.headers
    if DEBUG: print req.data
    if API_METHOD == 'post': req.get_method = lambda: 'POST'
    try:
        urllib2.urlopen(req)
        return True, ''
    except urllib2.HTTPError, e:
        error_response = e.read()
        if DEBUG: print e.code, error_response
        return False, error_response

def ip_post(params):
    data= urllib.urlencode(params)
    headers = {
            'Authorization' : 'Basic '+ base64.b64encode(D42_USERNAME + ':' + D42_PASSWORD),
            'Content-Type' : 'application/x-www-form-urlencoded'
        }
    req = urllib2.Request(D42_IP_API_URL, data, headers)
    if DEBUG: print '---REQUEST---',req.get_full_url()
    if DEBUG: print req.headers
    if DEBUG: print req.data
    if API_METHOD == 'post': req.get_method = lambda: 'POST'
    try:
        urllib2.urlopen(req)
        return True, ''
    except urllib2.HTTPError, e:
        error_response = e.read()
        if DEBUG: print e.code, error_response
        return False, error_response

def to_ascii(s): #not used in example, but provided incase you would need to convert certain values to ascii
    """remove non-ascii characters"""
    if type(s) == types.StringType:
        return s.encode('ascii','ignore')
    else:
        return str(s)

def changerow_to_api_args(row_values, header_row):
    args = {}
    for i, heading in enumerate(header_row):
        if row_values[i]: args.update({heading.strip().lower(): row_values[i].strip()})
    return args

def get_mac_addresses(row_values, header_row):
    macs = []
    for i, heading in enumerate(header_row):
        if heading == "macaddress":
            if row_values[i]: 
                macs.append(row_values[i].strip())
    return macs

def update_host_with_macs(hostname, macs):
    print "would update {} with macs {}".format(hostname, macs)
    for mac in macs:
        args = {"name":hostname, "macaddress":mac}
        post(args)

def get_ip_addresses(row_values, header_row):
    ips = []
    for i, heading in enumerate(header_row):
        if heading == "ipaddress":
            if row_values[i]:
                ips.append(row_values[i].strip())
    return ips

def update_host_with_ips(hostname, ips):
    print "would update {} with ips {}".format(hostname, ips)
    for ip in ips:
        args = {"device":hostname, "ipaddress":ip}
        ip_post(args)

def read_csv_parse_and_call_api_function(filename):
    notadded = []
    added = []
    with open(filename, 'rU') as csvfile:
        ReadLine = csv.reader(csvfile)
        header_row = ReadLine.next()
        for i in ReadLine:
            if i:
                try:
                    args = changerow_to_api_args(i, header_row)
                    hostname = args['name']
                    ADDED, msg = post(args)
                    macs = get_mac_addresses(i, header_row)
                    update_host_with_macs(hostname, macs)
                    ips = get_ip_addresses(i, header_row)
                    update_host_with_ips(hostname, ips)
                    if ADDED: added.append(i)
                    else: notadded.append(i+[' ',msg])
                except Exception, Err:
                    notadded.append(i+[str(Err),])
    print 'notadded %s' % notadded
    print 'added %s' % added

read_csv_parse_and_call_api_function(CSV_FILE_NAME)

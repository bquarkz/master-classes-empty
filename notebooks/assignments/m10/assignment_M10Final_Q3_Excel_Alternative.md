# M10 PMLS - Final Exam (Assignment)
## Q3. Note on tooling / Alternative used (Excel -> Google Sheets)

### Why this alternative

The assignment asks for a macro-enabled Excel workbook (`.xlsm`) with a **Submit button** that
calls the FastAPI `/predict` endpoint and displays, in the worksheet, the predicted probability
of default for every customer in the BankLoan test dataset (`TestData.csv`, 100 customers).

I do not have access to Windows or to a licensed/installed copy of Excel (desktop or Mac), so I
could not produce the requested `.xlsm` file. Excel Online was also considered, but it does not
support VBA/macros, so the "Submit button" requirement could not be met there either.

The closest equivalent I found, using only free and browser-based tools, is **Google Sheets +
Apps Script** (the same approach used for `assignment_M10U2_Excel_Alternative.txt`):
- Apps Script (Google's JavaScript-based macro language) plays the same role as VBA: it can call
  the deployed API and write the JSON response back into the sheet, attached to a drawing/shape,
  so clicking it behaves exactly like the requested Submit button.

This file documents, step by step, how to build and use that equivalent for the loan-default
`/predict` endpoint.

### Step 1: Deploy the API

1. Code: `assignment_M10Final_Q3.py` (same folder). It trains a `RandomForestClassifier`
   (`n_estimators=500`) on `BANK LOAN.csv` (dropping `SN`, target `DEFAULTER`) and exposes:
   - `GET /predict` - scores every customer in `TestData.csv` (the BankLoan test dataset) and
     returns one record per customer: `SN, AGE, EMPLOY, ADDRESS, DEBTINC, CREDDEBT, OTHDEBT,
     probability_of_default`. This is the endpoint the Submit button calls.
   - `POST /predict-customer` - optional extra endpoint to score one ad-hoc customer entered
     manually, for cases where the bank wants to test a new applicant that is not already in
     `TestData.csv`.
2. Add `fastapi`, `uvicorn`, and `scikit-learn` to `requirements.txt` (scikit-learn is already a
   project dependency), then deploy on Render with:
   - Build command: `pip install -r requirements.txt`
   - Start command: `uvicorn assignment_M10Final_Q3:app --host 0.0.0.0 --port $PORT`
3. Verify the live endpoint returns the 100 scored test customers:
       `https://<your-app-name>.onrender.com/predict`

### Step 2: Create the Google Sheet

1. Go to sheets.google.com -> Blank spreadsheet.
2. Rename it "M10 Final Exam - Bank Loan Default Prediction".
3. Name the first sheet "LoanDefaultPrediction" (this is where the scored test customers will be
   loaded).

### Step 3: Add the Apps Script (equivalent to the VBA macro)

1. In the sheet: `Extensions -> Apps Script`.
2. Paste the function below, which calls the deployed `/predict` endpoint, parses the JSON
   response (Apps Script does this natively, no JsonConverter.bas needed like in VBA), and writes
   headers + one row per customer into the sheet:

   ```javascript
   function submitLoanDefaultPrediction() {
     var url = "https://<your-app-name>.onrender.com/predict";
     var response = UrlFetchApp.fetch(url, { muteHttpExceptions: true });
     var data = JSON.parse(response.getContentText());

     var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("LoanDefaultPrediction");
     sheet.clear();

     var headers = ["SN", "AGE", "EMPLOY", "ADDRESS", "DEBTINC", "CREDDEBT", "OTHDEBT", "Probability of Default"];
     sheet.appendRow(headers);

     data.forEach(function (row) {
       sheet.appendRow([
         row.SN,
         row.AGE,
         row.EMPLOY,
         row.ADDRESS,
         row.DEBTINC,
         row.CREDDEBT,
         row.OTHDEBT,
         row.probability_of_default
       ]);
     });

     SpreadsheetApp.getUi().alert("Loan default predictions updated for " + data.length + " customers!");
   }
   ```

3. Save the project as "LoanDefaultPredictionScript".
4. Run it once from the Apps Script editor (`Run -> submitLoanDefaultPrediction`) to authorize
   the script's permission to call an external URL and edit the sheet (Google asks for this
   authorization only on the first run).

### Step 4: Add the Submit button

1. Back in the sheet: `Insert -> Drawing`.
2. Draw a simple rectangle with the text "Submit", then `Save and Close` to drop it onto the
   sheet (this is the Google Sheets equivalent of an Excel Form Control button).
3. Click the drawing once to select it, then click the 3-dot menu on its corner -> `Assign
   script` -> type `submitLoanDefaultPrediction` -> OK.

### Step 5: Use it

1. Click "Submit" - this calls the deployed `/predict` endpoint, which scores all 100 customers
   in `TestData.csv` with the Random Forest model and returns their probability of default.
2. The sheet is cleared and repopulated with the 8 columns (customer attributes + predicted
   probability of default), one row per customer.
3. The sheet was shared with "Anyone with the link - Viewer" so it can be opened without a
   Google account being required to request access.

### Mapping back to the original (Excel) requirements

| Excel requirement                                         | Google Sheets equivalent used                              |
|-------------------------------------------------------------|---------------------------------------------------------------|
| Macro-enabled workbook (`.xlsm`)                             | Google Sheets + bound Apps Script project                     |
| Load the BankLoan_Test dataset and estimate default probability | `/predict` scores `TestData.csv` with the Random Forest model |
| Submit button calls the FastAPI `/predict` endpoint           | `UrlFetchApp.fetch(url)` in Apps Script                        |
| Developer tab -> Insert -> Button (Form Control)              | `Insert -> Drawing` (shape/button)                             |
| Assign Macro to the button                                    | Assign script to the drawing                                   |
| Predicted probability displayed in the worksheet              | One row per customer written into the sheet, incl. probability |
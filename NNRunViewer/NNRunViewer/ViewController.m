//
//  ViewController.m
//  NNRunViewer
//
//  Created by Brad Patterson on 10/11/17.
//  Copyright © 2017 Brad Patterson. All rights reserved.
//

#import "ViewController.h"


@implementation ViewController

BOOL _nnRunning = false;
BOOL _nnAllVisualize = false;
NSTask *_nnRunTask;
NSTask *_nnVisAllTask;
NSTask *_nnClassifyTask;

-(void)parseAndUpdateStats:(NSString *)contents {
    NSArray *contentsArr = [contents componentsSeparatedByString:@"\n"];
    int currCount = 0;
    
    for (NSString *elem in contentsArr) {
        if ([elem isEqualToString:TOTAL_TIME_IDENT]) {
            [_totalTrainTimeStat setStringValue:[[contentsArr[currCount + 2] componentsSeparatedByString:@"I"][1] stringByAppendingString:@" seconds"]];
        }
        else if ([elem isEqualToString:NUM_TRAIN_IMG_IDENT]) {
            [_numTrainImgStat setStringValue:[contentsArr[currCount + 2] componentsSeparatedByString:@"I"][1]];
        }
        else if ([elem isEqualToString:NUM_VAL_IMG_IDENT]) {
            [_numValImgStat setStringValue:[contentsArr[currCount + 2] componentsSeparatedByString:@"I"][1]];
        }
        else if ([elem isEqualToString:NUM_EPOCH_IDENT]) {
            [_numEpochStat setStringValue:[contentsArr[currCount + 2] componentsSeparatedByString:@"I"][1]];
        }
        else if ([elem isEqualToString:VAL_IMG_PERCENT_IDENT]) {
            [_valPerStat setStringValue:[contentsArr[currCount + 2] componentsSeparatedByString:@"F"][1]];
        }
        else if ([elem isEqualToString:LAST_VAL_PERCENT_IDENT]) {
            [_valAccStat setStringValue:[[contentsArr[currCount + 2] componentsSeparatedByString:@"F"][1] stringByAppendingString: @" %"]];
        }
        else if ([elem isEqualToString:LAST_TRAIN_PERCENT_IDENT]) {
            [_testAccStat setStringValue:[[contentsArr[currCount + 2] componentsSeparatedByString:@"F"][1] stringByAppendingString: @" %"]];
        }
        
        currCount++;
        
    }
    
    
}

-(void)nnClassificationCompletion:(NSNotification *) notification {
    [_classifyPhotos setEnabled:true];
}

-(void)nnVisRunCompletion:(NSNotification *) notification {
    [_visAllNN setEnabled:true];
}

-(void)nnRunCompletion:(NSNotification *) notification {
    [_startNN setEnabled:true];
    [_nnRunStats removeAllItems];
    [_nnRunner removeAllItems];
    NSString *path = [[_projectWorkspace URL].path stringByAppendingString:@"/NNRuns/"];
    NSArray* dirs = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:path error:NULL];
    for (NSString* name in dirs) {
        NSString *extension = [name pathExtension];
        if ([extension isEqualToString:@""]) {
            if (![name isEqualToString:@".DS_Store"]) {
                [_nnRunner addItemWithObjectValue:name];
            }
        }

        if ([extension isEqualToString:@"nnRun"]) {
            [_nnRunStats addItemWithObjectValue:name];
        }
    }
}

- (void)classifyNN {
    [self showUserText:@"Setting up Classification"];
    _nnClassifyTask = [[NSTask alloc] init];
    _nnClassifyTask.launchPath = @"/usr/bin/python";
    NSString *resourcePath = [[NSBundle mainBundle] pathForResource:@"classification" ofType:@"py"];
    NSString *pathVar = [[[_projectWorkspace URL].path stringByAppendingString:@"/NNRuns/"] stringByAppendingString:[_nnRunner objectValueOfSelectedItem]];
    _nnClassifyTask.arguments = [NSArray arrayWithObjects: resourcePath, [_projectWorkspace URL].path, pathVar, nil];
    
    
    [_classifyPhotos setEnabled:false];
    
    [self showUserText:@"Running Classification"];
    [_nnClassifyTask launch];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(nnClassificationCompletion:)  name: NSTaskDidTerminateNotification object:_nnVisAllTask];
}

- (void)visAllNNRun {
    [self showUserText:@"Setting up Visualization"];
    _nnVisAllTask = [[NSTask alloc] init];
    _nnVisAllTask.launchPath = @"/usr/bin/python";
    NSString *resourcePath = [[NSBundle mainBundle] pathForResource:@"visualization" ofType:@"py"];
    _nnVisAllTask.arguments = [NSArray arrayWithObjects: resourcePath, [_projectWorkspace URL].path, nil];
    [_visAllNN setEnabled:false];
    [self showUserText:@"Running Visualization"];
    [_nnVisAllTask launch];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(nnVisRunCompletion:)  name: NSTaskDidTerminateNotification object:_nnVisAllTask];
}

- (void)showUserText:(NSString*)msg {
    [_userReportTextField setStringValue:
     [NSString stringWithFormat: @"%@\n %@", [_userReportTextField stringValue], msg]];
}

- (void)startRunningNN {
    [self showUserText:@"Setting up Neural Network"];
    if (_nnRunTask != NULL) {
        _nnRunTask = NULL;
    }
    _nnRunTask = [[NSTask alloc] init];
    _nnRunTask.launchPath = @"/usr/bin/python";
        NSString *resourcePath = [[NSBundle mainBundle] pathForResource:@"main" ofType:@"py"];
    int numEpochs = -1;
    int valPercent = -1;
    int valSteps = -1;
    int epochSteps = -1;
    int batchSize = -1;
    
    
    if ([_numEpochsUser intValue] <= 0) {
        [self showUserText:@"WARNING: The number of epochs entered is invalid. Please try to enter a number greater than 0. Using the default number of epochs"];
    }
    else {
        numEpochs = [_numEpochsUser intValue];
    }
    
    if ([_valPercentUser floatValue] <= 0 || [_valPercentUser floatValue] > 1) {
        [self showUserText:@"WARNING: The validation percentage entered is invalid. Please try to enter a number greater than 0 and less than 1. Using the default validation percentage."];
    }
    else {
        valPercent = [_valPercentUser floatValue];
    }
    
    if ([_valStepsUser floatValue] <= 0) {
        [self showUserText:@"WARNING: The validation steps entered is invalid. Please try to enter a number greater than 0. Using the default number of validation steps."];
    }
    else {
        valSteps = [_valStepsUser floatValue];
    }
    
    if ([_stepsEpochUser floatValue] <= 0) {
        [self showUserText:@"WARNING: The epoch steps entered is invalid. Please try to enter a number greater than 0. Using the default number of epoch steps."];
    }
    else {
        epochSteps = [_stepsEpochUser floatValue];
    }
    
    if ([_batchSizeUser floatValue] <= 0) {
        [self showUserText:@"WARNING: The batch size entered is invalid. Please try to enter a number greater than 0. Using the default batch size."];
    }
    else {
        batchSize = [_stepsEpochUser floatValue];
    }
    
    
    _nnRunTask.arguments = [NSArray arrayWithObjects: resourcePath, [_projectWorkspace URL].path, [NSString stringWithFormat:@"%d", numEpochs], [NSString stringWithFormat:@"%d", epochSteps], [NSString stringWithFormat:@"%d", valSteps], [NSString stringWithFormat:@"%d", valPercent],[NSString stringWithFormat:@"%d", batchSize], nil];
    [_startNN setEnabled:false];
   // [self routeOutputToWindow:_nnRunTask];
    [self showUserText:@"Running Neural Network"];
    [_nnRunTask launch];
    [[NSNotificationCenter defaultCenter] addObserver:self selector:@selector(nnRunCompletion:)  name: NSTaskDidTerminateNotification object:_nnRunTask];
}


- (IBAction)projWorkspaceOnClick:(id)sender {
    //Clear the options that are allowed for data pulling
    [_nnRunStats removeAllItems];
    [_nnRunner removeAllItems];
    NSString *path = [[_projectWorkspace URL].path stringByAppendingString:@"/NNRuns/"];
    NSArray* dirs = [[NSFileManager defaultManager] contentsOfDirectoryAtPath:path error:NULL];
    for (NSString* name in dirs) {
        NSString *extension = [name pathExtension];
        if ([extension isEqualToString:@""]) {
            if (![name isEqualToString:@".DS_Store"]) {
                [_nnRunner addItemWithObjectValue:name];
            }
           
        }
        if ([extension isEqualToString:@"nnRun"]) {
            [_nnRunStats addItemWithObjectValue:name];
            
        }
    }
}

- (IBAction)nnViewStatsOnClick:(id)sender {
    NSString *path = [[[_projectWorkspace URL].path stringByAppendingString:@"/NNRuns/"] stringByAppendingString:[_nnRunStats objectValueOfSelectedItem]];
    NSError *error;
    NSString *fileContents = [NSString stringWithContentsOfFile:path encoding:NSUTF8StringEncoding error:&error];
    if (error) {
        NSLog(@"Error reading file: %@", error.localizedDescription);
    }
    [self parseAndUpdateStats:fileContents];
}


- (IBAction)startNNOnClick:(NSButton *)sender {
    if (!_nnRunning) {
        [self startRunningNN];
    }
}


- (IBAction)visAllNNOnClick:(NSButton *)sender {
    if (!_nnAllVisualize) {
        [self visAllNNRun];
    }
}

- (IBAction)classifyPhotosOnClick:(NSButton *)sender {
    if (!_nnClassifyTask) {
        [self classifyNN];
    }
}


- (void)viewDidLoad {
    [_nnRunStats removeAllItems];
    [_nnRunner removeAllItems];
    [_userReportTextField setWraps:YES];
    [super viewDidLoad];
}


- (void)setRepresentedObject:(id)representedObject {
    [super setRepresentedObject:representedObject];

    // Update the view, if already loaded.
}


@end
